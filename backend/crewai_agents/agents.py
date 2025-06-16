# backend/crewai_agents/agents.py
from crewai import Agent
from crewai_agents.tools import buscar_novas_licitacoes, baixar_edital, extrair_texto_documento, salvar_dados_licitacao
from dotenv import load_dotenv
import os

load_dotenv()

# Configuração do LLM - para o MVP, pode ser OpenAI ou Google Gemini
# Certifique-se de que OPENAI_API_KEY ou GOOGLE_API_KEY esteja no seu .env

# Para OpenAI (Direto):
import openai
from openai import OpenAI
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CustomLLM:
    """Um wrapper simples para usar a API OpenAI diretamente como LLM para CrewAI."""
    def __init__(self, client):
        self.client = client
        self.model_name = "gpt-4o" # Ou "gpt-3.5-turbo"

    def chat_completion(self, messages, temperature, max_tokens):
        # Adapta a chamada da API OpenAI para o formato esperado pelo CrewAI
        # A CrewAI espera um objeto que se comporte como um LLM Langchain para o 'llm='
        # Para simplificar e remover langchain, estamos criando um wrapper mínimo.
        # No CrewAI 0.28.x, a integração direta com modelos é um pouco mais flexível.
        # Se houver problemas, a opção mais simples é usar langchain_openai, que é leve.
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                # Outros parâmetros podem ser adicionados conforme necessário
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Erro na chamada da API OpenAI: {e}")
            return "Ocorreu um erro ao processar a requisição."

llm_instance = CustomLLM(openai_client)


# Para Google Gemini (Direto, alternativa):
# import google.generativeai as genai
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#
# class CustomGeminiLLM:
#     """Um wrapper simples para usar a API Gemini diretamente como LLM para CrewAI."""
#     def __init__(self):
#         self.model = genai.GenerativeModel('gemini-pro')
#
#     def chat_completion(self, messages, temperature, max_tokens):
#         # Adapta as mensagens para o formato Gemini
#         gemini_messages = [{"role": "user", "parts": [msg['content']]} for msg in messages if msg['role'] == 'user']
#         # Você pode precisar de lógica mais complexa para o histórico de chat e roles no Gemini
#         try:
#             response = self.model.generate_content(
#                 contents=gemini_messages,
#                 generation_config=genai.types.GenerationConfig(
#                     temperature=temperature,
#                     max_output_tokens=max_tokens,
#                 )
#             )
#             return response.text
#         except Exception as e:
#             print(f"Erro na chamada da API Gemini: {e}")
#             return "Ocorreu um erro ao processar a requisição."
#
# llm_instance = CustomGeminiLLM()


class LicitacaoAgents:
    def __init__(self):
        # Passa a instância customizada do LLM para os agentes
        self.llm = llm_instance

    def coletor_de_editais(self):
        return Agent(
            role='Coletor de Editais',
            goal='Encontrar novas licitações no portal Comprasnet e baixar seus editais.',
            backstory="Sou especialista em web scraping e monitoramento de portais governamentais, garantindo que nenhum edital importante seja perdido.",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[buscar_novas_licitacoes, baixar_edital]
        )

    def analisador_basico_de_edital(self):
        return Agent(
            role='Analisador Básico de Edital',
            goal='Extrair os 5-7 campos-chave mais críticos de um edital e gerar um resumo conciso.',
            backstory="Com foco em eficiência, identifico rapidamente as informações essenciais de qualquer edital, transformando texto complexo em dados acionáveis.",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[extrair_texto_documento]
        )

    def estruturador_de_dados(self):
        return Agent(
            role='Estruturador de Dados de Licitações',
            goal='Consolidar e formatar os dados extraídos das licitações em um arquivo JSON padronizado para consumo posterior.',
            backstory="Minha missão é garantir que todos os dados coletados e analisados estejam organizados e prontos para serem usados em relatórios e dashboards.",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[salvar_dados_licitacao]
        )