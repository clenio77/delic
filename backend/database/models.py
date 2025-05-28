from sqlalchemy import Column, Integer, String, Text, Float
from backend.database.database import Base

class LicitacaoAnalysis(Base):
    __tablename__ = "licitacao_analysis"

    id = Column(Integer, primary_key=True, index=True)
    licitacao_id = Column(String, unique=True, index=True)
    description = Column(Text)
    status = Column(String, default="pending") # pending, analyzing, completed, failed
    suggested_price = Column(Float, nullable=True)
    spec_analysis = Column(Text, nullable=True)
    logistics_feedback = Column(Text, nullable=True)
    # Adicionar mais campos conforme a necessidade dos agentes