from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI # Ou ChatGoogleGenerativeAI, etc.
from backend.config import settings
from backend.agents.tools import market_price_search, analyze_specs_online

# Configurar o LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7, api_key=settings.OPENAI_API_KEY)
# ou para Google Gemini:
# llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, google_api_key=settings.GOOGLE_API_KEY)

class DelicAgents:
    def __init__(self):
        self.llm = llm # Usar o LLM configurado

    def price_analyst_agent(self):
        return Agent(
            role='Analista de Preços de Referência',
            goal=dedent("""
                Identificar os preços de referência mais realistas para bens e serviços em licitações,
                considerando variações cambiais e condições de mercado.
            """),
            backstory=dedent("""
                Especialista em análise de mercado e precificação, com profundo conhecimento
                das dinâmicas de custo e oferta-demanda, e experiência em licitações públicas.
            """),
            tools=[market_price_search],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def spec_analyst_agent(self):
        return Agent(
            role='Analista de Especificações Técnicas',
            goal=dedent("""
                Modernizar e garantir a clareza das especificações técnicas dos itens da licitação,
                evitando defasagens e ambiguidades.
            """),
            backstory=dedent("""
                Engenheiro com vasta experiência em produtos e normas técnicas, capaz de
                traduzir requisitos complexos em especificações claras e atualizadas.
            """),
            tools=[analyze_specs_online],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def logistics_analyst_agent(self):
        return Agent(
            role='Analista Logístico e de Prazos',
            goal=dedent("""
                Propor prazos de entrega e condições logísticas que sejam adequadas às realidades
                operacionais do mercado e às condições regionais.
            """),
            backstory=dedent("""
                Profissional de logística experiente em otimização de cadeias de suprimentos e
                gestão de riscos em transporte.
            """),
            # tools=[logistic_assessment_tool, regional_conditions_tool], # Exemplo de ferramentas futuras
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    # Adicionar outros agentes (Lote, Feedback, etc.)