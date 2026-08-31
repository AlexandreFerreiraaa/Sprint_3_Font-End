import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from backend import data_manager

st.set_page_config(page_title="Dados Brutos", page_icon="📈", layout="wide")

st.title("📈 Visualização de Dados de Sensores")

equipamentos = data_manager.get_equipamentos()

if not equipamentos:
    st.warning("Cadastre um equipamento primeiro para visualizar os dados.")
else:
    tags = [eq["TAG"] for eq in equipamentos]
    eq_selecionado = st.selectbox("Selecione o Equipamento para Monitoramento", tags)

    st.write(f"Monitorando sinais brutos e convertidos para: **{eq_selecionado}**")

    # Gerando dados mockados para simular a conversão (Volts, Ampères, RPM)
    # No futuro, isso virá do modelo/backend
    dados_mock = pd.DataFrame(
        np.random.randn(50, 3).cumsum(axis=0) + [220, 15, 1750], # Base values: 220V, 15A, 1750 RPM
        columns=['Tensão Convertida (V)', 'Corrente Convertida (A)', 'Rotação (RPM)']
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Tensão Atual", f"{dados_mock['Tensão Convertida (V)'].iloc[-1]:.2f} V")
    col2.metric("Corrente Atual", f"{dados_mock['Corrente Convertida (A)'].iloc[-1]:.2f} A")
    col3.metric("Rotação Atual", f"{int(dados_mock['Rotação (RPM)'].iloc[-1])} RPM")

    st.subheader("Histórico de Sinais")
    st.line_chart(dados_mock)