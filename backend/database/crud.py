from sqlalchemy.orm import Session
from backend.database import models

def create_licitacao_analysis(db: Session, licitacao_id: str, description: str):
    db_analysis = models.LicitacaoAnalysis(licitacao_id=licitacao_id, description=description)
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis

def get_licitacao_analysis(db: Session, licitacao_id: str):
    return db.query(models.LicitacaoAnalysis).filter(models.LicitacaoAnalysis.licitacao_id == licitacao_id).first()

def update_licitacao_analysis(db: Session, licitacao_id: str, **kwargs):
    db_analysis = db.query(models.LicitacaoAnalysis).filter(models.LicitacaoAnalysis.licitacao_id == licitacao_id).first()
    if db_analysis:
        for key, value in kwargs.items():
            setattr(db_analysis, key, value)
        db.commit()
        db.refresh(db_analysis)
    return db_analysis

def get_all_licitacao_reports(db: Session):
    return db.query(models.LicitacaoAnalysis).all()