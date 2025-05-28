from crewai import Task
from textwrap import dedent

class DelicTasks:
    def __init__(self, licitacao_description: str):
        self.licitacao_description = licitacao_description

    def analyze_price_task(self, agent):
        return Task(
            description=dedent(f"""
                Analise detalhadamente a descrição da licitação: '{self.licitacao_description}'.
                Utilize a ferramenta 'Market Price Search Tool' para obter o preço de mercado do(s)
                item(ns) principal(is) da licitação.
                Com base nisso, sugira um preço de referência realista e justificado para o DELIC.
                Concentre-se em como as variações cambiais podem afetar o preço.
            """),
            expected_output=dedent("""
                Um valor de preço de referência sugerido em R$ (formato numérico) e uma breve
                justificativa de como o preço foi determinado, considerando fatores de mercado e câmbio.
            """),
            agent=agent
        )

    def analyze_spec_task(self, agent):
        return Task(
            description=dedent(f"""
                Revise as especificações técnicas contidas na descrição da licitação:
                '{self.licitacao_description}'.
                Utilize a 'Specification Analysis Tool' para identificar qualquer defasagem,
                ambiguidade ou oportunidade de modernização.
                Sugira melhorias para tornar as especificações mais claras e atualizadas.
            """),
            expected_output=dedent("""
                Um texto conciso com as sugestões de modernização e clareza para as especificações
                técnicas, ou a confirmação de que estão adequadas.
            """),
            agent=agent
        )

    def analyze_logistics_task(self, agent):
        return Task(
            description=dedent(f"""
                Avalie as necessidades logísticas da licitação com base na descrição:
                '{self.licitacao_description}'.
                Considere o tipo de produto, volume e possíveis locais de entrega.
                Sugira prazos de entrega mais adequados às realidades operacionais do mercado e às
                condições regionais (se aplicável à descrição).
            """),
            expected_output=dedent("""
                Um texto descrevendo os prazos de entrega e quaisquer observações logísticas importantes,
                como sugestões para otimizar a distribuição ou considerações regionais.
            """),
            agent=agent
        )

    # Adicionar outras tarefas (Lote, Feedback, etc.)