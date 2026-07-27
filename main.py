import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from crew_logic import run_investment_crew
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Comitê de Investimentos IA", page_icon=":money_with_wings:", layout="wide")
st.title("Comitê de Investimentos IA :money_with_wings:")
st.write("Bem-vindo ao Comitê de Investimentos IA! Insira o ticker da ação que deseja analisar.")

if not os.getenv("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY") == "GEMINI_API_KEY":
    st.error("Por favor, configure a variável de ambiente GEMINI_API_KEY no arquivo .env.")
    st.stop()

ticker_input = st.text_input("Digite o ticker da ação (ex: PETR4.SA, ITUB4.SA, AAPL):")

if st.button("Analisar"):
    with st.spinner(f"Os agentes estão analisando {ticker_input}..."):
        try:
            relatorio_final = run_investment_crew(ticker_input)
            st.success("Análise concluída!")
            st.markdown("### Relatório gerado com sucesso!")
            st.markdown("----")
            st.markdown(relatorio_final.raw if hasattr(relatorio_final, 'raw') else str (relatorio_final))
        except Exception as e:
            st.error(f"Erro ao executar a análise: {e}")
