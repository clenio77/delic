# backend/crewai_agents/tools.py
from crewai.tools import tool
from web_scraping.mcp_playwright import download_licitacao_edital, search_new_licitacoes_comprasnet
from web_scraping.document_processor import extract_text_from_document # ALTERADO
import json
import os

@tool("Buscar Novas Licitações no Comprasnet")
def buscar_novas_licitacoes(search_url: str) -> str:
    """
    Tool CrewAI: Busca novas licitações em um portal (ex: Comprasnet).
    Retorna uma lista de URLs de licitações encontradas em formato JSON.
    """
    print(f"Agente: Buscando novas licitações em {search_url}...")
    licitacoes = search_new_licitacoes_comprasnet(search_url=search_url)
    return json.dumps(licitacoes)

@tool("Baixar Edital")
def baixar_edital(url: str) -> str:
    """
    Tool CrewAI: Baixa o arquivo do edital de uma URL específica ou retorna o caminho local.
    Retorna o caminho do arquivo baixado ou local.
    """
    print(f"Agente: Tentando baixar edital de {url}...")
    download_path = "backend/data/raw_licitacoes"
    file_path = download_licitacao_edital(url, download_path)
    if file_path:
        return file_path
    return "Erro ao baixar edital ou link não encontrado."

@tool("Extrair Texto de Documento")
def extrair_texto_documento(file_path: str) -> str:
    """
    Tool CrewAI: Extrai o conteúdo de texto de um arquivo de edital (PDF/DOCX).
    Retorna o texto limpo do documento.
    """
    print(f"Agente: Extraindo texto de {file_path}...")
    text_content = extract_text_from_document(file_path)
    if text_content:
        return text_content
    return "Não foi possível extrair texto do documento."

@tool("Salvar Dados da Licitação")
def salvar_dados_licitacao(data_json: str) -> str:
    """
    Tool CrewAI: Salva os dados extraídos de uma licitação em um arquivo JSON.
    Acumula os resultados, evitando duplicatas simples por ID.
    """
    file_path = "backend/data/processed_licitacoes.json"
    
    # Garante que a pasta exista
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        new_data = json.loads(data_json)
        
        # Tenta carregar dados existentes
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        # Adiciona novos dados. Evitar duplicatas simples no MVP por ID.
        if new_data.get('id') and new_data['id'] not in [d.get('id') for d in existing_data]:
            existing_data.append(new_data)
        else:
            print(f"Dados da licitação com ID {new_data.get('id')} já existem ou ID ausente. Não adicionado.")
            return f"Dados da licitação com ID {new_data.get('id')} já existem ou ID ausente."

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)
        print(f"Dados da licitação salvos em: {file_path}")
        return f"Dados da licitação salvos com sucesso em {file_path}"
    except json.JSONDecodeError:
        return "Erro: Formato JSON inválido."
    except Exception as e:
        return f"Erro ao salvar dados da licitação: {e}"