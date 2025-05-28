from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from backend.api import schemas
from backend.database import crud, database
from backend.agents.crew_manager import DelicAnalysisCrew
import re # Para extrair o preço sugerido do texto

router = APIRouter(
    prefix="/licitacoes",
    tags=["Licitacoes"],
)

@router.post("/analyze", response_model=schemas.LicitacaoAnalysisResponse)
async def start_licitacao_analysis(
    request: schemas.LicitacaoAnalysisRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(database.get_db)
):
    db_analysis = crud.get_licitacao_analysis(db, request.licitacao_id)
    if db_analysis:
        if db_analysis.status == "pending" or db_analysis.status == "analyzing":
            raise HTTPException(status_code=400, detail="Análise para esta licitação já em andamento.")
        # Opcional: permitir reanálise, resetando o status
        crud.update_licitacao_analysis(db, request.licitacao_id, status="pending",
                                       suggested_price=None, spec_analysis=None, logistics_feedback=None)
    else:
        db_analysis = crud.create_licitacao_analysis(db, request.licitacao_id, request.description)
    
    # Iniciar a análise em segundo plano
    background_tasks.add_task(run_analysis_crew, db_analysis.licitacao_id, request.description, db)
    
    return db_analysis

def run_analysis_crew(licitacao_id: str, description: str, db: Session):
    # Nota: Precisamos de uma nova sessão DB para cada tarefa de fundo
    # Ou gerenciar a sessão de forma assíncrona.
    # Para MVP, vamos criar uma nova sessão aqui.
    db_session_for_task = database.SessionLocal()
    try:
        crew = DelicAnalysisCrew(licitacao_id, description)
        crud.update_licitacao_analysis(db_session_for_task, licitacao_id, status="analyzing")
        
        result = crew.run()
        print(f"Resultado final da crew: {result}")

        # Processar o resultado da crew para atualizar o DB
        suggested_price = None
        price_match = re.search(r'Preço de referência sugerido em R\$ ([\d,.]+)', result)
        if price_match:
            try:
                suggested_price = float(price_match.group(1).replace('.', '').replace(',', '.'))
            except ValueError:
                pass # Em caso de falha na conversão

        spec_analysis_output = "Análise de especificações concluída." # Simplificado para MVP
        logistics_output = "Análise logística concluída." # Simplificado para MVP

        crud.update_licitacao_analysis(
            db_session_for_task,
            licitacao_id,
            status="completed",
            suggested_price=suggested_price,
            spec_analysis=spec_analysis_output,
            logistics_feedback=logistics_output
        )
    except Exception as e:
        print(f"Erro na execução da crew para licitação {licitacao_id}: {e}")
        crud.update_licitacao_analysis(db_session_for_task, licitacao_id, status="failed")
    finally:
        db_session_for_task.close()

# Rota para obter relatórios
@router.get("/reports", response_model=list[schemas.LicitacaoAnalysisResponse])
def get_reports(db: Session = Depends(database.get_db)):
    return crud.get_all_licitacao_reports(db)