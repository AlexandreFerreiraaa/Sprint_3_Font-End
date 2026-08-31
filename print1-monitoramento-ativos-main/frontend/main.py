import streamlit as st
import pandas as pd
import sys
import os
import time

# Adiciona o diretório raiz ao path para importar o backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend import data_manager

# Configuração da página em modo Wide
st.set_page_config(page_title="Inteligência Operacional | Forzy", page_icon="⚙️", layout="wide")

# Estilização visual para os cards de alerta com cores semânticas
st.markdown("""
<style>
    .alert-card-critical {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
        color: #721c24;
    }
    .alert-card-warning {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
        color: #856404;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚙️ Painel de Alertas e Estados Operacionais")
st.markdown("Acompanhamento contínuo de anomalias integrado com Machine Learning e Processamento de Linguagem Natural (NLP).")

# Gerenciamento de estado para simular a atualização via botão
if "atualizado" not in st.session_state:
    st.session_state.atualizado = False

col_btn, col_info = st.columns([1, 4])
with col_btn:
    if st.button("🔄 Atualizar Alertas", type="primary"):
        with st.spinner("Sincronizando com modelos analíticos..."):
            time.sleep(0.8)
            st.session_state.atualizado = not st.session_state.atualizado
        st.success("Painel atualizado!")

with col_info:
    st.info("Status: Conectado à camada de análise preditiva.")

st.divider()

# Métricas Principais (Cores Semânticas)
m1, m2, m3 = st.columns(3)
with m1:
    st.metric(label="Ativos Monitorados", value="18", delta="Estável")
with m2:
    st.metric(label="Alertas Críticos", value="2" if st.session_state.atualizado else "1", delta="+1 anomalia" if st.session_state.atualizado else "0", delta_color="inverse")
with m3:
    st.metric(label="Avisos de Atenção", value="3", delta="Normal")

st.markdown("### 🧠 Resumos Inteligentes (NLP) & Alertas Ativos")

col_left, col_right = st.columns([2, 1])

with col_left:
    # Alerta Crítico Principal
    st.markdown("""
    <div class="alert-card-critical">
        <strong>[CRÍTICO] Motor Principal #04 - Vibração Anômala Detectada</strong><br>
        <em>Resumo NLP:</em> Identificado desvio severo na frequência de vibração do mancal. Indício de desalinhamento mecânico.<br>
        <strong>Ação Recomendada:</strong> Programar inspeção imediata e reduzir carga em 25%.
    </div>
    """, unsafe_allow_html=True)
    
    # Alerta dinâmico que aparece ao clicar no botão
    if st.session_state.atualizado:
        st.markdown("""
        <div class="alert-card-critical">
            <span style="float: right; font-size: 0.8em;">Agora mesmo</span>
            <strong>[CRÍTICO] Compressor de Alta Pressão #02 - Sobreaquecimento</strong><br>
            <em>Resumo NLP:</em> Aumento repentino de temperatura de 12°C acima da linha de base operacional.<br>
            <strong>Ação Recomendada:</strong> Verificar fluxo do sistema de refrigeração secundário.
        </div>
        """, unsafe_allow_html=True)

    # Alerta de Atenção
    st.markdown("""
    <div class="alert-card-warning">
        <strong>[ATENÇÃO] Gerador Auxiliar #01 - Flutuação de Tensão</strong><br>
        <em>Resumo NLP:</em> Oscilações leves na corrente elétrica fora do padrão nominal histórico durante o ciclo.<br>
        <strong>Ação Recomendada:</strong> Monitorar comportamento nas próximas 2 horas.
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("#### 💡 Apoio à Decisão")
    with st.expander("🛠️ Recomendações", expanded=True):
        st.markdown("- **Prioridade 1:** Acionar equipe mecânica para o **Motor #04**.")
        st.markdown("- **Prioridade 2:** Checar telemetria do **Compressor #02**[cite: 1].")
    
    st.markdown("#### 📊 Saúde Global")
    st.progress(78, text="Operacionalidade: 78%")

st.divider()

# Carrega e exibe os equipamentos cadastrados do backend (mantendo a funcionalidade original)
equipamentos = data_manager.get_equipamentos()
if equipamentos:
    df = pd.DataFrame(equipamentos)
    st.subheader("📋 Base de Equipamentos Cadastrados")
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.info("Nenhum equipamento cadastrado ainda. Utilize o menu lateral para adicionar.")