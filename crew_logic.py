import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from stock_tools import fetch_stock_data

load_dotenv()

# Garante que a google key está visivel globalmente
api_key = os.getenv("GEMINI_API_KEY")
if api_key :
    os.environ["GEMINI_API_KEY"] = api_key
    os.environ["GOOGLE_API_KEY"] = api_key

# Instancia o LLM do Gemini
gemini_llm = LLM(
    model=f"gemini/{os.getenv('GEMINI_MODEL_NAME', 'gemini-3.1-flash-lite')}",
        api_key=api_key,
        request_timeout=120,
        config=dict(
            temperature=0.7
        )
)

def run_investment_crew(ticker_symbol: str) -> str:
    # Agente Quantitativo
    agente_quant = Agent(
         role="Analista Quantitativo Sênior",
                         goal=f"Analisar o preço atual e o histórico recente da ação {ticker_symbol}.",
                         backstory="Você é um analista meticuloso. Usa ferramentas para extrair dados reais e analisa tendências.",
                         verbose=True,
                         allow_delegation=False,
                         tools=[fetch_stock_data],
                         llm=gemini_llm
        )

    # Agente Gestor
    agente_redator = Agent(
        role="Gestor de Portifólio",
                goal=f"Criar um relatório executivo sobre {ticker_symbol} baseado nos dados quantitativos.",
                backstory="Você é um Diretor de Investimentos. Transforma análises técnicas em recomendações claras e com linguagem de fácil entendimento para o cliente que não possui linguagem técnica.",
                verbose=True,
                allow_delegation=False,
                tools=[fetch_stock_data],
                llm=gemini_llm
        )

    # Tarefas
    tarefa_dados = Task(
            description=f"Use a ferramenta 'Buscar Dados da Bolsa' para pegar o histórico da ação {ticker_symbol}.",
            expected_output="Um resumo numérico dos últimos 5 dias e a tendência do ativo.",
            agent=agente_quant
        )

    tarefa_relatorio = Task(
        description=f"Com base na análise quantitativa, escreva um relatório final recomendando cautela ou otimismo para {ticker_symbol}.",
        expected_output="Relatório em Markdown com Título, Resumo dos Dados e Conclusão Executiva.",
        agent=agente_redator
    )

    # Orquestração da equipe
    crew = Crew(
        agents=[agente_quant, agente_redator],
        tasks=[tarefa_dados, tarefa_relatorio],
        process=Process.sequential,
        max_rpm=10,
        verbose=True
    )

    return crew.kickoff()
