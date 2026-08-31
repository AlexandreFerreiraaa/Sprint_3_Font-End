import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json
import os

# Configuração da página
st.set_page_config(page_title="Dashboard Operacional", page_icon="📊", layout="wide")

st.title("📊 Dashboard Operacional de Ativos")

# Função para carregar os dados dos equipamentos salvos na Sprint anterior
@st.cache_data
def carregar_equipamentos():
    caminho_json = os.path.join("data", "equipamentos.json")
    if os.path.exists(caminho_json):
        with open(caminho_json, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

equipamentos = carregar_equipamentos()

if not equipamentos:
    st.error("Arquivo 'data/equipamentos.json' não encontrado ou está vazio. Verifique a pasta 'data'.")
    st.stop()

# Extrai a lista de TAGs reais diretamente do JSON
lista_tags = [eq["TAG"] for eq in equipamentos]

# 1. Navegação por Planta/Área (Sidebar)
st.sidebar.header("Navegação")
planta = st.sidebar.selectbox("Selecione a Planta/Área", ["Planta Principal - Setor Automotivo"])
selected_tag = st.sidebar.selectbox("Selecione o Equipamento (TAG)", lista_tags)

# Busca as especificações do motor selecionado no JSON
motor_atual = next((eq for eq in equipamentos if eq["TAG"] == selected_tag), None)

if motor_atual:
    st.subheader(f"Monitoramento em Tempo Real: {selected_tag}")

    # 2. Alertas e Status Baseados em Limites Operacionais
    # Configuração de simulação para a jornada do operador no vídeo
    if selected_tag == "MOT-1102":
        status = "Crítico"
        st.error(f"Status do Ativo: {status} 🔴 - Risco de Falha Iminente (Vibração Elevada)")
        vibracao_base = 13.8
        temp_base = 94.2
    else:
        status = "Saudável"
        st.success(f"Status do Ativo: {status} 🟢 - Operação Normal")
        vibracao_base = 1.9
        temp_base = 56.1

    # Exibição de Métricas Rápidas (Telemetria)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Temperatura Atual", value=f"{temp_base:.1f} °C", delta="Crítico" if status == "Crítico" else "Estável", delta_color="inverse")
    with col2:
        st.metric(label="Vibração Geral", value=f"{vibracao_base:.1f} mm/s", delta="Alerta" if status == "Crítico" else "Normal", delta_color="inverse")
    with col3:
        st.metric(label="Tensão do Ativo", value=f"{motor_atual.get('Tensão (V)', 760)} V")

    st.markdown("---")

    # 3. Gráficos Temporais (Séries Temporais) - Corrigido freq="h"
    st.subheader("Análise de Tendência (Séries Temporais)")

    # Gerando histórico com base no comportamento do motor escolhido
    datas = pd.date_range(start="2026-06-16", periods=24, freq="h")
    np.random.seed(42)  # Mantém a consistência dos gráficos ao alternar abas
    vibracao_historica = np.random.normal(loc=vibracao_base, scale=0.8, size=24)
    temperatura_historica = np.random.normal(loc=temp_base, scale=2.5, size=24)

    df_telemetria = pd.DataFrame({
        "Data": datas, 
        "Vibração (mm/s)": vibracao_historica, 
        "Temperatura (°C)": temperatura_historica
    })

    # Construção do gráfico interativo com Plotly
    fig = px.line(df_telemetria, x="Data", y=["Vibração (mm/s)", "Temperatura (°C)"], 
                  title=f"Evolução de Parâmetros nas últimas 24h — {selected_tag}",
                  markers=True)

    # Linha de corte do limite crítico de temperatura
    fig.add_hline(y=85, line_dash="dash", line_color="red", annotation_text="Limite Crítico de Temperatura (85°C)")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

# 4. Integração de Cadastro Visual
    with st.expander("🔍 Ver Cadastro Técnico e Imagem da Placa"): 
        # O título do botão vai acima. O código abaixo fica dentro do bloco:
        col_dados, col_img = st.columns([1, 1])
        
        with col_dados:
            st.markdown("### Especificações Técnicas (Dados do JSON)")
            st.markdown(f"**Fabricante:** {motor_atual.get('Fabricante', 'Não identificado')}")
            st.markdown(f"**Modelo:** {motor_atual.get('Modelo', 'Não identificado')}")
            st.markdown(f"**Potência:** {motor_atual.get('Potência (W)', 0)} W")
            st.markdown(f"**Tensão:** {motor_atual.get('Tensão (V)', 0)} V")
            
        with col_img:
            st.markdown("### Imagem da Placa Cadastrada")
            # Dica: use '/' em vez de '\' ou coloque um 'r' antes da string para evitar erros de caminho
            st.image(r"A:/images.jpg", caption="Placa do Motor")