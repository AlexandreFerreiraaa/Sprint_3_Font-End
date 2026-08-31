import streamlit as st
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from backend import data_manager

st.set_page_config(page_title="Cadastro Técnico", page_icon="📋")

st.title("📋 Cadastro Técnico de Equipamento")
st.write("Preencha a ficha técnica do motor.")

with st.form("form_cadastro"):
    col1, col2 = st.columns(2)
    
    with col1:
        tag = st.text_input("TAG de Identificação", placeholder="Ex: MOT-001")
        fabricante = st.text_input("Fabricante", placeholder="Ex: WEG")
        potencia = st.number_input("Potência (W)", min_value=0.0, step=100.0)
        
    with col2:
        modelo = st.text_input("Modelo")
        tensao = st.selectbox("Tensão (V)", options=[220, 380, 440, 760])

    submit = st.form_submit_button("Salvar Equipamento", type="primary")

if submit:
    if not tag or not modelo:
        # Cores semânticas: Erro
        st.error("Por favor, preencha a TAG e o Modelo.")
    else:
        # Latência forçada para UX (Human-in-the-loop/Feedback visual)
        with st.spinner("Registrando equipamento no banco de dados..."):
            time.sleep(1) # Simulando tempo de rede/processamento
            data_manager.add_equipamento(tag, modelo, fabricante, potencia, tensao)
        
        # Cores semânticas: Sucesso
        st.success(f"Equipamento {tag} cadastrado com sucesso!")