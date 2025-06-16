# Correios Licitações 

Sistema MVP para monitoramento, análise e exibição de licitações dos Correios, com backend FastAPI, frontend React e pipeline de processamento automatizado.

---

## Sumário

- [Visão Geral](#visão-geral)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Deploy no Render](#deploy-no-render)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Build e Execução Local](#build-e-execução-local)
- [Pipeline de Processamento de Licitações](#pipeline-de-processamento-de-licitações)
- [Endpoints da API](#endpoints-da-api)
- [Dicas e Observações](#dicas-e-observações)

---

## Visão Geral

- **Backend:** FastAPI + CrewAI (Python)
- **Frontend:** React (Node.js)
- **Pipeline:** Agentes CrewAI para scraping, análise e estruturação de licitações
- **Deploy:** Docker multi-stage (ideal para Render)

---

## Estrutura do Projeto

```
correios_licitacoes_mvp/
  backend/
    api/                # FastAPI (servidor e endpoints)
    crewai_agents/      # Agentes, tasks e pipeline CrewAI
    data/               # Dados processados e editais brutos
    web_scraping/       # Funções de scraping e processamento de documentos
  frontend/
    src/                # Código React
    public/             # index.html
  Dockerfile            # Build multi-stage para backend+frontend
  requirements.txt      # Dependências Python
  README.md             # (Este arquivo)
```

---

## Deploy no Render

### 1. **Configuração do Serviço**

- **Tipo:** Web Service
- **Runtime:** Docker
- **Build Command:** (deixe em branco, o Dockerfile já faz tudo)
- **Start Command:** (deixe em branco, o Dockerfile já define o CMD)
- **Porta:** 8000

### 2. **Variáveis de Ambiente**

No painel do Render, adicione as seguintes variáveis:

| Nome              | Descrição                                 | Exemplo                         |
|-------------------|-------------------------------------------|---------------------------------|
| OPENAI_API_KEY    | Chave da API OpenAI (para LLM)            | sk-...                          |
| (ou) GOOGLE_API_KEY | Chave da API Google Gemini (opcional)   | ...                             |

> **Obs:** O sistema usa por padrão OpenAI. Para usar Gemini, ajuste o código conforme instruções nos comentários do arquivo `backend/crewai_agents/agents.py`.

### 3. **Deploy**

- Faça push do projeto para o GitHub.
- Conecte o repositório ao Render.
- Clique em "Deploy".

---

## Build e Execução Local

### **Pré-requisitos**

- Docker instalado **OU**
- Python 3.10+, Node.js 18+ (para desenvolvimento local)

### **Com Docker**

```bash
docker build -t licitacoes-mvp .
docker run -p 8000:8000 --env OPENAI_API_KEY=sk-... licitacoes-mvp
```

### **Sem Docker (desenvolvimento)**

1. **Backend**
   ```bash
   cd backend
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r ../requirements.txt
   uvicorn api.app:app --reload
   ```

2. **Frontend**
   ```bash
   cd frontend
   npm install
   npm start
   ```

---

## Pipeline de Processamento de Licitações

Para processar novos editais e popular o sistema:

1. Coloque arquivos `.pdf` ou `.docx` de editais em `backend/data/raw_licitacoes/`.
2. Ajuste o caminho do arquivo de exemplo em `backend/crewai_agents/main.py` se necessário.
3. Execute o pipeline:
   ```bash
   cd backend
   python3 crewai_agents/main.py
   ```
4. O resultado será salvo em `backend/data/processed_licitacoes.json` e exibido no frontend.

---

## Endpoints da API

- `GET /api`  
  Teste simples: retorna `{"Hello": "World"}`

- `GET /api/licitacoes`  
  Retorna a lista de licitações processadas (JSON).

---

## Dicas e Observações

- **LLM:** O sistema depende de uma chave válida da OpenAI (ou Gemini, se configurado).
- **Playwright:** O scraping real pode exigir dependências extras e configuração de navegador no ambiente Render. Para MVP, use arquivos locais.
- **Frontend:** O React é servido pelo próprio backend FastAPI em produção (via Dockerfile).
- **Customização:** Para processar múltiplos editais, adapte o pipeline para iterar sobre todos os arquivos em `raw_licitacoes/`.

---

## Dependências

### **Backend (requirements.txt)**
```
crewai
crewai-tools
python-dotenv
fastapi
uvicorn
playwright
beautifulsoup4
pandas
openai
pypdf
python-docx
```

### **Frontend (package.json)**
- react
- react-dom
- react-scripts

---

## Variáveis de Ambiente

Crie um arquivo `.env` (ou configure no Render):

```
OPENAI_API_KEY=sk-...
# GOOGLE_API_KEY=...
```

---

## Suporte

Dúvidas ou problemas?  
Abra uma issue no repositório ou entre em contato!

---

Se quiser um exemplo de `.env` ou instruções para scraping real, me avise!
