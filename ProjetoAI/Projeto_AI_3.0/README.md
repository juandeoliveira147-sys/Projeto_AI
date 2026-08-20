# 🤖 AI 3.0 — Assistente Virtual em Python

> Assistente virtual desenvolvido em Python, com **PostgreSQL** para armazenamento de dados e **Ollama + Llama 3.1** para conversação com Inteligência Artificial.

A **AI 3.0** é uma evolução das versões anteriores do projeto, buscando transformar um simples programa de terminal em um assistente virtual capaz de **armazenar informações do usuário, manter histórico de conversas, gerenciar lembretes, conversar utilizando IA e executar ferramentas próprias**.

O projeto também utiliza **Programação Orientada a Objetos**, separando as principais responsabilidades em diferentes classes.

---

# 📌 Sobre o projeto

A AI 3.0 funciona como um assistente virtual executado pelo terminal.

Ao iniciar pela primeira vez, o programa solicita algumas informações do usuário, como:

* Nome
* Idade

Essas informações são armazenadas no **PostgreSQL**.

Nas próximas inicializações, a AI consulta o banco de dados e reconhece o usuário automaticamente.

Além disso, o sistema possui:

* 🧠 Memória persistente
* 💬 Conversação com IA
* 📝 Histórico de conversas
* ⏰ Sistema de lembretes
* 🧮 Calculadora
* 🎯 Jogo de adivinhação
* 🎲 Respostas aleatórias para determinadas situações
* 🗄️ Banco de dados PostgreSQL
* 🤖 Modelo de linguagem local através do Ollama

---

# 🛠️ Tecnologias utilizadas

| Tecnologia    | Utilização                             |
| ------------- | -------------------------------------- |
| 🐍 Python     | Linguagem principal                    |
| 🐘 PostgreSQL | Banco de dados                         |
| 🦙 Ollama     | Execução local do modelo de IA         |
| 🧠 Llama 3.1  | Modelo utilizado na conversação        |
| 🔗 LangChain  | Integração entre Python e Ollama       |
| `psycopg2`    | Conexão do Python com PostgreSQL       |
| `random`      | Respostas aleatórias e números do jogo |
| `datetime`    | Data utilizada no contexto da IA       |
| `time`        | Controle de pausas e fluxo do programa |

---

# 🏗️ Arquitetura da AI 3.0

A AI 3.0 possui uma arquitetura modular baseada em classes.

```text
                         ┌──────────────────────┐
                         │       USUÁRIO        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       AI_V3.py      │
                         │                      │
                         │      MENU DA AI     │
                         └──────────┬───────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
     ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
     │   Calculadora   │   │ Adivinhe número │   │   Conversação   │
     │                 │   │                 │   │                 │
     │ + - * / // % ** │   │ 1 → 100         │   │    Ollama       │
     └─────────────────┘   │ 1 → 1000        │   │    Llama 3.1    │
                           │ 1 → 10000       │   └────────┬────────┘
                           └─────────────────┘            │
                                                         │
                                                         ▼
                                              ┌─────────────────────┐
                                              │    PostgreSQL       │
                                              │                     │
                                              │ • Nome              │
                                              │ • Idade             │
                                              │ • Histórico         │
                                              │ • Lembretes         │
                                              └─────────────────────┘
```

---

# 🧩 Estrutura das classes

O arquivo `AI_V3.py` possui quatro classes principais.

```text
AI_V3.py
│
├── coracao_da_AI
│      │
│      ├── carregar()
│      ├── primeiro_acesso()
│      ├── memoria()
│      ├── lembretes()
│      └── conversar()
│
├── calculadora
│      │
│      ├── primeiro_numero()
│      ├── escolher_operacao()
│      ├── segundo_numero()
│      ├── divisor()
│      └── menu_calculadora()
│
├── adivinhe_o_numero
│      │
│      ├── menu_do_jogo()
│      └── nivel()
│
└── menu_da_AI
       │
       ├── bem_vindo()
       └── menu()
```

### ❤️ `coracao_da_AI`

É o núcleo principal do sistema.

É responsável por:

* Inicializar a aplicação
* Verificar se existe memória no banco
* Realizar o primeiro cadastro
* Recuperar informações do usuário
* Recuperar lembretes
* Gerenciar a conversação com o Ollama
* Salvar o histórico
* Salvar novos lembretes

---

### 🧮 `calculadora`

Responsável pelas operações matemáticas.

Operações disponíveis:

```text
+
-
x
*
/
//
**
%
```

Também possui tratamento para divisão por zero e entradas inválidas.

---

### 🎯 `adivinhe_o_numero`

Implementa o jogo de adivinhação.

Existem três níveis:

```text
Nível 1 → 1 até 100
Nível 2 → 1 até 1.000
Nível 3 → 1 até 10.000
```

O programa fornece dicas indicando se o número escolhido está acima ou abaixo do número secreto.

---

### 📋 `menu_da_AI`

É responsável pela navegação principal do programa.

O usuário pode escolher entre:

```text
Calculadora
Adivinhe o número
Conversar
Lembretes
Sair
```

---

# 🐘 PostgreSQL

A AI 3.0 utiliza PostgreSQL para armazenar os dados persistentes do usuário.

O arquivo:

```text
bancodedadosAI.py
```

é responsável pela conexão com o banco.

A conexão é feita através do `psycopg2`.

---

# 🗄️ Banco de dados

O banco utilizado pelo projeto deve se chamar:

```text
bancodedadosdaAI
```

A tabela principal utilizada pela aplicação é:

```text
bancodedadosdaAI
```

Ela possui atualmente os seguintes campos:

```text
nome
idade
historico
lembretes
```

Representação:

```text
┌──────────────────────────────────────┐
│         bancodedadosdaAI             │
├──────────────────────────────────────┤
│ nome       VARCHAR(100)              │
│ idade      INTEGER                    │
│ historico  TEXT                       │
│ lembretes  TEXT                       │
└──────────────────────────────────────┘
```

---

# 🔄 Fluxo do banco de dados

Ao iniciar o programa:

```text
                AI_V3.py
                    │
                    ▼
          coracao_da_AI.carregar()
                    │
                    ▼
             conectar()
                    │
                    ▼
             PostgreSQL
                    │
             ┌──────┴──────┐
             │             │
             ▼             ▼
        Existe dados?    Não existe?
             │             │
            SIM            NÃO
             │             │
             ▼             ▼
        Recupera       Primeiro
         memória       acesso
             │             │
             └──────┬──────┘
                    ▼
              Menu da AI
```

---

# 🧠 Sistema de memória

Uma das principais características da AI 3.0 é a capacidade de manter informações mesmo depois que o programa é encerrado.

Por exemplo:

```text
Usuário:
Meu nome é Juan.

AI:
Olá Juan! Prazer em conhecer você.
```

O nome é armazenado no PostgreSQL.

Quando o programa for aberto novamente:

```text
AI → PostgreSQL → Recupera nome → "Olá Juan!"
```

Isso permite que a AI mantenha uma memória persistente.

---

# 💬 Sistema de conversação

A conversa utiliza:

```text
Python
   │
   ▼
LangChain
   │
   ▼
Ollama
   │
   ▼
Llama 3.1
```

O modelo recebe um contexto construído pela aplicação.

Esse contexto contém:

```text
Data atual
       +
Lembretes
       +
Histórico
       +
Nome do usuário
       +
Informações sobre o usuário
       +
Pergunta atual
```

Então o modelo gera a resposta.

---

# 🔄 Fluxo da conversação

```text
Usuário
   │
   │ pergunta
   ▼
coracao_da_AI.conversar()
   │
   ├──────────────► PostgreSQL
   │                    │
   │                    ├── Nome
   │                    ├── Histórico
   │                    └── Lembretes
   │
   ▼
ChatPromptTemplate
   │
   ▼
Ollama
   │
   ▼
Llama 3.1
   │
   ▼
Resposta
   │
   ├──────────────► Atualiza histórico
   │
   └──────────────► Atualiza lembretes
   │
   ▼
Usuário
```

---

# ⏰ Sistema de lembretes

A AI 3.0 possui um sistema de lembretes integrado à conversação.

Por exemplo:

```text
Usuário:
Me lembre de fazer o dever às 19h.
```

A IA recebe instruções específicas no prompt para identificar essa solicitação.

Quando um novo lembrete é identificado, o modelo retorna uma instrução especial:

```text
REMANEJAR_LEMBRETES:
```

O Python identifica essa informação e atualiza os lembretes no PostgreSQL.

```text
Ollama
   │
   ▼
REMANEJAR_LEMBRETES:
   │
   ▼
Python identifica
   │
   ▼
Atualiza variável
   │
   ▼
UPDATE PostgreSQL
   │
   ▼
Lembrete salvo
```

---

# 💾 Histórico de conversas

A AI também mantém um histórico da conversa.

Após cada interação, o sistema adiciona:

```text
Usuário: pergunta

AI: resposta
```

Esse histórico é armazenado no PostgreSQL.

Nas próximas interações, o histórico é enviado novamente ao modelo como parte do contexto.

```text
PostgreSQL
     │
     ▼
Histórico
     │
     ▼
Prompt
     │
     ▼
Ollama
     │
     ▼
Nova resposta
```

---

# 🎮 Funcionalidades disponíveis

### 🧠 Assistente

* [x] Conversação com Llama 3.1
* [x] Contexto temporal
* [x] Nome do usuário
* [x] Histórico de conversas
* [x] Memória persistente
* [x] Lembretes

### 🧮 Ferramentas

* [x] Calculadora
* [x] Jogo de adivinhação
* [x] Sistema de níveis no jogo
* [x] Respostas aleatórias

### 🗄️ Banco de dados

* [x] Cadastro inicial
* [x] PostgreSQL
* [x] Recuperação de dados
* [x] Armazenamento de histórico
* [x] Armazenamento de lembretes

---

# 📁 Estrutura atual do projeto

```text
AI-3.0/
│
├── AI_V3.py
│
├── bancodedadosAI.py
│
└── README.md
```

### `AI_V3.py`

Contém a lógica principal da aplicação:

* Assistente
* Menu
* Calculadora
* Jogo
* Conversação
* Memória
* Lembretes

### `bancodedadosAI.py`

Contém a conexão com o PostgreSQL:

```python
conectar()
encerrar_conexao()
```

---

# ⚙️ Instalação

## 1. Clone o projeto

```bash
git clone https://github.com/juandeoliveira147-sys/AI-3.0.git
cd AI-3.0
```

---

## 2. Instale as dependências

```bash
pip install psycopg2
pip install langchain-ollama
pip install langchain-core
```

Ou, caso o projeto possua um `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

# 🐘 3. Configure o PostgreSQL

Instale o PostgreSQL e crie um banco de dados chamado:

```text
bancodedadosdaAI
```

Depois, abra:

```text
bancodedadosAI.py
```

e altere:

```python
password = "sua_senha_aqui"
```

para a senha do seu usuário PostgreSQL.

Também verifique:

```python
user = "postgres"
host = "127.0.0.1"
port = "5432"
database = "bancodedadosdaAI"
```

> ⚠️ **Importante:** não publique sua senha real no GitHub. O ideal é futuramente utilizar variáveis de ambiente (`.env`) para proteger as credenciais do banco.

---

# 🦙 4. Configure o Ollama

Instale o Ollama e certifique-se de que ele está funcionando.

Depois, baixe o modelo utilizado pela AI 3.0:

```bash
ollama pull llama3.1
```

Verifique os modelos instalados:

```bash
ollama list
```

A aplicação utiliza:

```python
OllamaLLM(model="llama3.1")
```

---

# ▶️ 5. Execute a AI

Depois de configurar o PostgreSQL e o Ollama:

```bash
python AI_V3.py
```

---

# 🔐 Segurança

Este projeto possui atualmente as credenciais do banco configuradas diretamente no arquivo Python.

Para utilizar o projeto em um ambiente público, recomenda-se alterar essa arquitetura para utilizar variáveis de ambiente.

Exemplo futuro:

```text
.env
│
├── DB_USER
├── DB_PASSWORD
├── DB_HOST
├── DB_PORT
└── DB_NAME
```

E adicionar o `.env` ao:

```text
.gitignore
```

para impedir que credenciais sejam enviadas para o GitHub.

---

# 🔗 Versões anteriores

A AI 3.0 faz parte de uma evolução contínua do projeto.

### 🤖 AI 1.0

> **Link:** `https://github.com/juandeoliveira147-sys/Projeto_AI/tree/d577e97e5dbb9087e51988ed1e63f4958cf45e92/ProjetoAI/Projeto_AI_1.0`

### 🤖 AI 2.0

> **Link:** `https://github.com/juandeoliveira147-sys/Projeto_AI/tree/d577e97e5dbb9087e51988ed1e63f4958cf45e92/ProjetoAI/Projeto_AI_2.0`

### 🤖 AI 3.0

> **Versão atual deste repositório**

---

# 🚀 Evolução do projeto

```text
AI 1.0
  │
  ▼
AI 2.0
  │
  ▼
AI 3.0
  │
  ├── PostgreSQL
  ├── Ollama
  ├── Llama 3.1
  ├── LangChain
  ├── Memória persistente
  ├── Histórico
  ├── Lembretes
  ├── Calculadora
  └── Jogos
  │
  ▼
AI 4.0
  │
  └── Próxima evolução
```

---

# 🎯 Objetivo do projeto

A AI 3.0 não tem como objetivo ser apenas um chatbot.

O projeto foi desenvolvido para estudar e aplicar, na prática, conceitos de:

* Python
* Programação Orientada a Objetos
* Banco de dados
* SQL
* PostgreSQL
* Integração com Inteligência Artificial
* Modelos de linguagem locais
* LangChain
* Persistência de dados
* Modularização
* Tratamento de erros
* Lógica de programação

A proposta é continuar evoluindo a AI conforme novos conhecimentos são adquiridos, transformando gradualmente o projeto em um **assistente virtual cada vez mais completo**.

---

# 👨‍💻 Autor

**Juan De Oliveira**

Projeto desenvolvido como parte do aprendizado prático de **Python, Banco de Dados e Inteligência Artificial**.

---

## ⭐ Status do projeto

🚧 **Em desenvolvimento**

A AI 3.0 continuará recebendo novas funcionalidades, melhorias de arquitetura e integrações conforme o projeto evolui.
