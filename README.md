# 💰 Comitê de Investimentos IA

Aplicação web que simula um pequeno comitê de investimentos usando **agentes de IA autônomos** (multi-agent system). O usuário informa o ticker de uma ação, e dois agentes — um analista quantitativo e um gestor de portfólio — trabalham em sequência para gerar um relatório executivo de investimento.

## Como funciona

1. O usuário digita o ticker de uma ação (ex: `PETR4`, `AAPL`) na interface Streamlit
2. O **Agente Quantitativo** usa uma ferramenta de busca de dados reais (Yahoo Finance) para levantar o preço atual e o histórico dos últimos 5 dias
3. O **Agente Gestor de Portfólio** recebe essa análise e escreve um relatório executivo em linguagem acessível, recomendando cautela ou otimismo
4. O resultado é exibido na tela, formatado em Markdown

Os dois agentes são orquestrados pelo **CrewAI** em um processo sequencial (`Process.sequential`): a saída do primeiro agente vira entrada do segundo.

## Tecnologias

- **Python**
- **CrewAI** — orquestração dos agentes de IA e definição de ferramentas (`@tool`)
- **Google Gemini** — modelo de linguagem usado pelos agentes
- **yfinance** — busca de dados reais da bolsa de valores
- **Streamlit** — interface web
- **python-dotenv** — gerenciamento de variáveis de ambiente

## Arquitetura

```
├── main.py           # Interface Streamlit e ponto de entrada
├── crew_logic.py      # Definição dos agentes, tarefas e orquestração (CrewAI)
├── stock_tools.py      # Ferramenta de busca de dados da bolsa (yfinance)
├── requirements.txt
└── .env                # Variáveis de ambiente (não versionado)
```

## Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/tiagoaugustofonseca/comite-investimentos-ia.git
cd comite-investimentos-ia
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
GEMINI_API_KEY=sua-chave-aqui
GEMINI_MODEL_NAME=gemini-3.1-flash-lite
```

Você pode gerar uma chave gratuita em [Google AI Studio](https://aistudio.google.com/apikey).

### 5. Rode a aplicação

```bash
streamlit run main.py
```

Acesse `http://localhost:8501` no navegador.

## Possíveis melhorias futuras

- Adicionar um terceiro agente de análise de risco/volatilidade
- Cachear resultados de tickers já consultados recentemente
- Adicionar testes automatizados para as ferramentas (`stock_tools.py`)
- Permitir comparação entre múltiplos tickers na mesma análise

## Autor

**Tiago Augusto Fonseca**
[LinkedIn](https://www.linkedin.com/in/tiago-augusto-fonseca) · [GitHub](https://github.com/tiagoaugustofonseca)