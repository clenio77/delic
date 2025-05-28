from crewai import Crew, Process
from backend.agents.agents import DelicAgents
from backend.agents.tasks import DelicTasks

class DelicAnalysisCrew:
    def __init__(self, licitacao_id: str, licitacao_description: str):
        self.licitacao_id = licitacao_id
        self.licitacao_description = licitacao_description
        self.agents = DelicAgents()
        self.tasks = DelicTasks(licitacao_description)

    def run(self):
        price_analyst = self.agents.price_analyst_agent()
        spec_analyst = self.agents.spec_analyst_agent()
        logistics_analyst = self.agents.logistics_analyst_agent()

        analyze_price_task = self.tasks.analyze_price_task(price_analyst)
        analyze_spec_task = self.tasks.analyze_spec_task(spec_analyst)
        analyze_logistics_task = self.tasks.analyze_logistics_task(logistics_analyst)

        crew = Crew(
            agents=[price_analyst, spec_analyst, logistics_analyst],
            tasks=[analyze_price_task, analyze_spec_task, analyze_logistics_task],
            process=Process.sequential, # Ou hierarchical para tarefas mais complexas
            verbose=2 # Nível de detalhe do log da Crew
        )

        print(f"\n--- Iniciando Análise da Licitação {self.licitacao_id} ---")
        result = crew.kickoff()
        print(f"\n--- Análise da Licitação {self.licitacao_id} Concluída ---")
        return result