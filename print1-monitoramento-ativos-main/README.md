# 🏭 Gestão e Monitoramento de Ativos - Sprints 1 & 2
Integrantes:
• Luca Tiepolo Schmidt Morete - RM560255
• Alexandre Ferreira - RM 565626
• Carlos Bucker - RM 555812
• Filipe Melo - RM 564571

Este repositório contém a evolução do sistema de monitoramento de ativos industriais. O projeto evoluiu de uma base de cadastro técnico para um dashboard de telemetria operacional com análise visual de dados.

## 🚀 O que foi entregue (Sprint 2)

Nesta etapa, o foco foi a **Digitalização Visual**:
- **Dashboard Operacional:** Interface interativa para monitoramento em tempo real.
- **Telemetria:** Visualização de vibração e temperatura.
- **Alertas Inteligentes:** Indicadores de status (Saudável/Crítico) via cores e métricas.
- **Rastreabilidade:** Integração dinâmica com o cadastro via JSON e exibição de placas (OCR).

## 📁 Estrutura do Projeto

```text
projeto_monitoramento/
├── backend/
│   └── data_manager.py
├── frontend/
│   ├── main.py              # Tela de navegação
│   └── pages/               
│       ├── 1_📋_Cadastro.py
│       ├── 2_📈_Dados_Brutos.py
│       └── 3_📊_Dashboard.py  # NOVO: Interface de Monitoramento
├── data/
│   └── equipamentos.json    # Dados dos ativos
└── requirements.txt

🛠 Tecnologias
Front-end: Streamlit

Visualização: Plotly

Manipulação de Dados: Pandas / JSON

* **Objetivo da Sprint 2:** Desenvolver interface de monitoramento operacional com foco na experiência do usuário e visibilidade de falhas.
* **Solução Técnica:**
    * *Visualização:* Utilização do **Streamlit** para rápida prototipagem e **Plotly** para gráficos de séries temporais (vibração e temperatura).
    * *Lógica:* Implementação de filtros (selectbox) que consultam o JSON de equipamentos e atualizam dinamicamente os gráficos e os estados de alerta (verde/vermelho).
* **Destaque :** A interface permite que o operador identifique uma falha em milissegundos através da mudança visual do status (o requisito de UX/UI).

---