import yfinance as yf
from crewai.tools import tool

@tool ("Buscar dados da Bolsa")
def fetch_stock_data(ticker: str) -> str:
    """
    Busca o preço atual e o histórico dos últimos 5 dias de uma ação na bolsa.
    Passe o ticker da ação (ex: PETR4.SA, ITUB4.SA, AAPL).
    """
    try:
        if not ticker.endswith("SA") and not ticker.isalpha():
            ticker += ".SA"
        stock = yf.Ticker(ticker)
        hist = stock.history(period="5d")

        if hist.empty:
            return f"Não foi possível encontrar dados para o ticker {ticker}."

        last_price = hist['Close'].iloc[-1]

        resumo = f"Dados recentes para {ticker}:\n"
        resumo += f"Preço atual de Fechamento: R$ {last_price:.2f}\n\n"

        resumo += "Histórico dos últimos 5 dias (Preço de Fechamento):\n"
        resumo += hist['Close'].to_string()

        return resumo
    except Exception as e:
        return f"Erro ao buscar dados: {str(e)}"