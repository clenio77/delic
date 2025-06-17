# backend/crewai_agents/tasks.py
from crewai import Task
from textwrap import dedent

class LicitacaoTasks:
    """
    Define as tarefas (Tasks) do pipeline CrewAI para licitações:
    - Buscar licitações
    - Baixar e extrair edital
    - Analisar edital
    - Salvar dados processados
    Cada método retorna uma Task CrewAI configurada para o agente correspondente.
    """
    def __init__(self, agent_instance):
        self.agent_instance = agent_instance # Para acessar as ferramentas do agente

    def buscar_licitacoes_task(self, agent, search_url: str):
        """
        Task: Busca URLs de licitações no portal informado usando a tool de busca.
        """
        return Task(
            description=dedent(f"""
                Use a ferramenta 'Buscar Novas Licitações no Comprasnet' para encontrar URLs de licitações
                no portal {search_url}.
                Identifique no mínimo 1 URL de edital para processamento.
                """),
            expected_output=dedent("""
                Uma lista JSON de URLs de licitações encontradas, ex:
                [{"id": "licitacao_X", "url": "https://..."}]
                """),
            agent=agent,
        )

    def baixar_e_extrair_edital_task(self, agent, licitacao_url: str):
        """
        Task: Baixa o edital da URL e extrai o texto do documento usando as tools apropriadas.
        """
        return Task(
            description=dedent(f"""
                Use a ferramenta 'Baixar Edital' para fazer o download do edital da URL: {licitacao_url}.
                Após o download, use a ferramenta 'Extrair Texto de Documento' para obter o texto limpo do edital.
                """),
            expected_output=dedent(f"""
                O caminho do arquivo do edital baixado e o texto completo extraído do edital.
                Exemplo: 'caminho/do/edital.pdf', 'Conteúdo do edital...'
                """),
            agent=agent,
        )

    def analisar_edital_basico_task(self, agent, edital_content: str, licitacao_url: str):
        """
        Task: Analisa o texto do edital e extrai campos-chave, gerando um JSON estruturado.
        """
        return Task(
            description=dedent(f"""
                Analise o conteúdo do edital fornecido abaixo para extrair os seguintes campos-chave:
                - Objeto da Licitação (resumo conciso)
                - Data de Abertura das Propostas (formato DD/MM/AAAA)
                - Prazo de Entrega da Proposta (se explícito)
                - Valor Estimado (apenas números, se presente. Ex: 1500000.00 ou "Não informado")
                - Requisito de Habilitação Principal (ex: 'Certidão Negativa de Débitos Federais' ou 'Registro no CRA')
                - Link Original do Edital (a URL que o originou: {licitacao_url})

                Gere um resumo conciso (2-3 frases) do edital.

                Formate o resultado como um objeto JSON. Assegure-se que o ID seja um identificador único para a licitação
                (ex: baseado na URL ou um ID gerado).
                Exemplo de JSON de saída:
                ```json
                {{
                    "id": "licitacao_id_unica",
                    "objeto": "Descrição concisa do objeto.",
                    "data_abertura": "DD/MM/AAAA",
                    "prazo_proposta": "X dias/meses" ou "Não informado",
                    "valor_estimado": 1234567.89,
                    "requisito_habilitacao_principal": "Descrição do requisito",
                    "resumo": "Resumo em 2-3 frases.",
                    "link_original": "{licitacao_url}"
                }}
                ```
                Certifique-se que o JSON é válido.
                Conteúdo do Edital:
                ---
                {edital_content}
                ---
                """),
            expected_output=dedent("""
                Um objeto JSON contendo os campos-chave extraídos e o resumo,
                com um ID único para a licitação e o link original.
                """),
            agent=agent,
        )

    def salvar_dados_task(self, agent, data_json: str):
        """
        Task: Salva o JSON de dados da licitação processada usando a tool apropriada.
        """
        return Task(
            description=dedent(f"""
                Use a ferramenta 'Salvar Dados da Licitação' para persistir o JSON de dados
                da licitação processada.
                """),
            expected_output="Confirmação de que os dados foram salvos com sucesso no arquivo JSON.",
            agent=agent,
        )