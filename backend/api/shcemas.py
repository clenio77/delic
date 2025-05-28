from pydantic import BaseModel, Field

class LicitacaoAnalysisRequest(BaseModel):
    licitacao_id: str = Field(..., example="LIC-2024-001")
    description: str = Field(..., example="Aquisição de computadores para escritórios regionais.")

class LicitacaoAnalysisResponse(BaseModel):
    id: int
    licitacao_id: str
    description: str
    status: str
    suggested_price: float | None = None
    spec_analysis: str | None = None
    logistics_feedback: str | None = None

    class Config:
        from_attributes = True # updated from orm_mode = True for Pydantic v2