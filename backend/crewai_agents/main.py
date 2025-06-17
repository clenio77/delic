# backend/crewai_agents/main.py
from crewai import Crew, Process
from crewai_agents.agents import LicitacaoAgents
from crewai_agents.tasks import LicitacaoTasks
import json
import os
from dotenv import load_dotenv

load_dotenv()

def run_licitacao_crew():
    """
    Executa o pipeline CrewAI para processar um edital de exemplo:
    1. Extrai o texto do edital (PDF/DOCX) local.
    2. Analisa o texto e extrai campos-chave.
    3. Salva o resultado em JSON para consumo pelo frontend.
    """
    print("Iniciando a Crew de Gestão de Licitações MVP...")

    # Instancia os agentes e as tarefas
    agents = LicitacaoAgents()
    tasks = LicitacaoTasks(agents)

    # Define os agentes
    coletor_agente = agents.coletor_de_editais()
    analisador_agente = agents.analisador_basico_de_edital()
    estruturador_agente = agents.estruturador_de_dados()

    # Para o MVP, vamos usar um edital de teste.
    # VOCÊ DEVE SUBSTITUIR ISSO POR UMA URL REAL DE UM EDITAL DO COMPRASNET
    # E GARANTIR QUE O download_licitacao_edital NO tools.py FUNCIONE PARA ELA.
    # OU SIMPLIFICAR CRIANDO UM ARQUIVO PDF/DOCX MANUALMENTE NA PASTA raw_licitacoes.
    # Vamos simular passando uma URL de edital diretamente.

    # Crie um arquivo PDF ou DOCX de exemplo e coloque em backend/data/raw_licitacoes/edital_exemplo_mvp.pdf
    # E coloque a URL original do edital abaixo para que o Agente Analisador possa referenciá-la
    exemplo_edital_local_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/raw_licitacoes/edital_exemplo_mvp.docx'))
    exemplo_edital_original_url = "https://www.comprasnet.gov.br/seguro/licitacao_portal_detalhe.asp?coduasg=999999&numprp=1234567890&tipo=Preg%E3o&Origem=Portal&TipoEnvio=A&numitem=1&ordenador=1" # URL dummy

    print(f"[DEBUG] Caminho absoluto do edital de exemplo: {exemplo_edital_local_path}")

    if not os.path.exists(exemplo_edital_local_path):
        print(f"ATENÇÃO: Edital de exemplo '{exemplo_edital_local_path}' não encontrado.")
        print("Por favor, baixe um edital de teste (PDF/DOCX) do Comprasnet e salve-o nesse caminho.")
        print("A Crew não poderá rodar sem ele para o MVP.")
        return

    # Tarefa 1: Extrair texto do edital de exemplo
    extrair_texto_task = tasks.baixar_e_extrair_edital_task(
        agent=coletor_agente, # Coletor para extrair o texto, pois a ferramenta está nele
        licitacao_url=exemplo_edital_local_path # Passando o caminho local para simular o download
    )

    # Tarefa 2: Analisar o edital e extrair informações
    analisar_task = tasks.analisar_edital_basico_task(
        agent=analisador_agente,
        edital_content=extrair_texto_task.output, # O resultado da tarefa anterior é o input
        licitacao_url=exemplo_edital_original_url # Passa a URL original para o JSON final
    )

    # Tarefa 3: Salvar os dados processados
    salvar_task = tasks.salvar_dados_task(
        agent=estruturador_agente,
        data_json=analisar_task.output # O resultado da análise é o input
    )

    # Cria a Crew com o processo sequencial
    crew = Crew(
        agents=[coletor_agente, analisador_agente, estruturador_agente],
        tasks=[extrair_texto_task, analisar_task, salvar_task],
        process=Process.sequential,
        verbose=True, # Nível de detalhe da execução
        full_output=True,
        max_rpm=29 # Limita as requisições por minuto ao LLM para evitar exceder cotas
    )

    # Executa a Crew
    result = crew.kickoff()

    print("\n--- Processamento da Crew Finalizado ---")
    print(result)

if __name__ == "__main__":
    # Garanta que a pasta de dados brutos exista
    os.makedirs("backend/data/raw_licitacoes", exist_ok=True)
    # Exemplo de uso:
    # Crie manualmente um arquivo PDF ou DOCX em backend/data/raw_licitacoes/edital_exemplo_mvp.pdf
    # antes de rodar este script.
    run_licitacao_crew()