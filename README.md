**Sistema de Agentes Inteligentes DELIC**

Este projeto tem como objetivo principal otimizar e automatizar os processos de licitação do Departamento de Licitações e Contratações Diretas (DELIC) dos Correios, utilizando agentes inteligentes. A iniciativa surge da necessidade de aprimorar continuamente os processos de contratação, abordando desafios identificados em licitações fracassadas, como variações cambiais, dificuldades logísticas, defasagem de especificações técnicas e incertezas quanto ao sistema de registro de preços.

O sistema visa incorporar as sugestões de melhoria do mercado fornecedor, incluindo a atualização de preços de referência, modernização das especificações técnicas, prazos de entrega mais adequados e melhor estruturação dos lotes.

***Visão Geral do Projeto***

O sistema é modular, composto por três serviços principais que se comunicam para orquestrar e executar análises de licitações:

***Frontend (Vue.js):***  Interface de usuário intuitiva para interação com o sistema.

***Backend API (FastAPI):***  Lógica de negócios e comunicação entre o frontend e os agentes inteligentes.
Agentes Inteligentes (CrewAI): Núcleo de inteligência, onde os agentes autônomos realizam as análises e geram insights.

***Banco de Dados (PostgreSQL):***  Persistência de dados estruturados do sistema.
Variáveis de Ambiente (.env): Gerenciamento de configurações e chaves de API.
Problemas Abordados
Com base na análise de licitações fracassadas entre janeiro de 2024 e janeiro de 2025, o sistema aborda os seguintes desafios identificados pelo mercado fornecedor:

***Variações Cambiais:***  Dificultam a precificação precisa.
Dificuldades Logísticas: Impactam os prazos e custos de entrega.
Defasagem de Especificações Técnicas: Geram incerteza e propostas inadequadas.
Incertezas quanto ao Sistema de Registro de Preços: Afetam a participação das empresas.
Soluções Propostas com Agentes Inteligentes
O projeto implementa agentes inteligentes para fornecer as seguintes melhorias, conforme sugerido pelas empresas:

**** Atualização de Preços de Referência:***  Agentes analisarão dados de mercado e flutuações cambiais para sugerir preços mais realistas.
Modernização e Clareza nas Especificações Técnicas: Agentes revisarão e proporão melhorias nas especificações, eliminando defasagens e ambiguidades.
Prazos de Entrega Adequados: Agentes avaliarão as condições logísticas e regionais para sugerir prazos mais realistas.
Melhor Estruturação dos Lotes: Agentes considerarão as condições regionais e as características dos produtos para otimizar a divisão dos lotes.

**Tecnologias Utilizadas** 

***Frontend:***
Vue.js: Framework progressivo para construção de interfaces de usuário reativas.
Vuetify: Framework de componentes UI para Vue.js, baseado no Material Design, garantindo uma interface moderna e responsiva.
Axios: Cliente HTTP para comunicação com a API de backend.
Vue Router: Gerenciamento de rotas para navegação entre as páginas do aplicativo.

**Backend:**

FastAPI: Framework Python moderno, rápido e de alta performance para construção de APIs RESTful.
Pydantic: Para validação e serialização de dados.
SQLAlchemy: ORM (Object-Relational Mapper) para interação com o banco de dados PostgreSQL.
Uvicorn: Servidor ASGI para executar a aplicação FastAPI.

***Agentes Inteligentes:***

CrewAI: Framework para orquestração de agentes autônomos e colaborativos.
CrewAI-Tools: Biblioteca para dar ferramentas aos agentes (web scraping, acesso a APIs, etc.).
LangChain / OpenAI / Google Gemini: Modelos de Linguagem Grandes (LLMs) para o "cérebro" dos agentes (necessário configurar sua chave de API).
Playwright: Biblioteca para automação de navegador (web scraping headless), utilizada pelas ferramentas dos agentes.
python-dotenv: Para gerenciar variáveis de ambiente de forma segura.

***Banco de Dados:***

PostgreSQL: Banco de dados relacional robusto e escalável.
Banco de Dados Vetorial (ex: ChromaDB, Weaviate - sugestão para funcionalidades futuras): Para implementação de RAG (Retrieval Augmented Generation), permitindo que os agentes consultem grandes volumes de documentos para contextualização.
Containerização:
Docker: Para empacotar e isolar os serviços em ambientes consistentes.
Docker Compose: Para definir e executar aplicações multi-container.

**Estrutura do Projeto**

seu_projeto_delic/
├── frontend/             # Código fonte da aplicação Vue.js
│   ├── public/           # Arquivos estáticos
│   ├── src/              # Código fonte principal do Vue
│   │   ├── assets/       # Imagens, estilos globais
│   │   ├── components/   # Componentes Vue reutilizáveis
│   │   ├── views/        # Telas/páginas da aplicação
│   │   ├── App.vue       # Componente raiz
│   │   ├── main.js       # Ponto de entrada do Vue
│   │   └── router.js     # Configuração de rotas
│   ├── package.json      # Dependências do frontend
│   └── vite.config.js    # Configuração do Vite
├── backend/              # Código fonte da API FastAPI e lógica dos agentes
│   ├── api/              # Endpoints da API
│   │   ├── routers/      # Rotas separadas (e.g., licitacoes.py, auth.py)
│   │   ├── schemas.py    # Modelos de dados Pydantic
│   │   └── main.py       # Ponto de entrada da API FastAPI
│   ├── agents/           # Definição dos agentes CrewAI, tarefas e ferramentas
│   │   ├── agents.py     # Definição dos agentes
│   │   ├── tasks.py      # Definição das tarefas
│   │   ├── tools.py      # Ferramentas que os agentes usam
│   │   └── crew_manager.py # Orquestrador da Crew
│   ├── database/         # Configuração do banco de dados e modelos ORM
│   │   ├── database.py   # Configuração da conexão DB
│   │   ├── models.py     # Modelos SQLAlchemy
│   │   └── crud.py       # Operações CRUD
│   ├── config.py         # Configurações do backend
│   └── requirements.txt  # Dependências Python do backend
├── docker-compose.yml    # Configuração dos serviços Docker
├── .env                  # Variáveis de ambiente (não versionado)
└── README.md             # Este arquivo
Como Iniciar o Projeto (MVP)
Siga estes passos para configurar e rodar o projeto em seu ambiente local usando Docker Compose:

Pré-requisitos:

Docker Desktop (ou Docker Engine e Docker Compose CLI) instalado.
Uma chave de API da OpenAI (ou Google Gemini, se preferir) para os LLMs.
Clone o Repositório:

Bash

git clone <URL_DO_SEU_REPOSITORIO>
cd seu_projeto_delic
Crie o arquivo de Variáveis de Ambiente:

Na raiz do projeto (seu_projeto_delic/), crie um arquivo chamado .env.
Adicione as seguintes variáveis, substituindo os valores pelos seus:
Fragmento do código

DATABASE_URL="postgresql://user:password@db:5432/delic_db"
OPENAI_API_KEY="sk-SUA_CHAVE_OPENAI_AQUI"
# GOOGLE_API_KEY="SUA_CHAVE_GEMINI_AQUI" # Descomente e use se optar por Gemini
user e password são as credenciais do seu banco de dados PostgreSQL. Para este MVP, são os mesmos definidos no docker-compose.yml.
db é o nome do serviço do banco de dados no docker-compose.yml.
Inicie os Serviços com Docker Compose:

No terminal, na raiz do projeto, execute:
Bash

docker-compose up --build
Este comando irá construir as imagens Docker para o frontend e backend, baixar a imagem do PostgreSQL e iniciar todos os serviços. Pode levar alguns minutos na primeira vez.
Acesse a Aplicação:

Uma vez que todos os serviços estiverem rodando:
Frontend (Vue.js): Abra seu navegador e acesse http://localhost:5173.
Backend API (FastAPI - Docs): Você pode acessar a documentação interativa da API em http://localhost:8000/docs.
Próximos Passos e Melhorias
Este MVP fornece uma base sólida. Para um sistema de produção, as seguintes melhorias são cruciais:

Autenticação e Autorização Completas: Implementar um sistema robusto de login de usuário e controle de acesso baseado em papéis (RBAC) no backend (FastAPI) e protegê-lo no frontend (Vue.js).
Tratamento de Erros: Adicionar tratamento de erros mais robusto em todas as camadas (frontend, backend, agentes) e mecanismos de logging detalhados.
Validação de Dados: Fortalecer a validação de entrada de dados no frontend e backend para evitar dados inválidos.
Testes: Implementar testes unitários, de integração e end-to-end para garantir a confiabilidade do sistema.
Mecanismos de Fila/Mensageria: Para tarefas de análise de agentes que podem levar tempo, integrar uma fila de mensagens (ex: Celery com RabbitMQ/Redis) para processamento assíncrono e feedback em tempo real para o usuário.
Banco de Dados Vetorial: Implementar um banco de dados vetorial (como ChromaDB, Weaviate ou Pinecone) para RAG, permitindo que os agentes consultem informações de documentos extensos (PDFs de editais, normas, histórico).
Monitoramento e Logs: Configurar ferramentas de monitoramento (ex: Prometheus, Grafana) e um sistema de agregação de logs (ex: ELK Stack) para observar o desempenho do sistema e dos agentes.
Deploy para Produção: Configurar o deploy da aplicação em um ambiente de nuvem (AWS, Google Cloud, Azure) com CI/CD.
Expansão dos Agentes: Adicionar mais agentes e tarefas conforme as necessidades do DELIC (ex: Agente de Lotes, Agente de Feedback para o SRP).
Interface do Usuário: Aprimorar a interface do usuário com mais funcionalidades, filtros, gráficos avançados e uma experiência de usuário mais rica.
Contribuição
Contribuições são bem-vindas! Se você tiver ideias ou quiser colaborar, por favor, sinta-se à vontade para abrir issues ou pull requests.

Boas Contratações!