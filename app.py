import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Análise de Viabilidade Construtiva", layout="wide")

st.title("🏗️ Análise de Viabilidade Construtiva")
st.markdown("Preencha as informações abaixo para gerar o relatório preliminar de viabilidade construtiva.")

# Seções do questionário
st.header("1️⃣ Identificação do Projeto e do Cliente")
proprietarios = st.text_input("Nome dos proprietários")
endereco = st.text_input("Endereço do terreno")
objetivo = st.selectbox("Objetivo do projeto", ["Residência própria", "Investimento", "Locação"])
orcamento = st.number_input("Orçamento disponível (R$)", min_value=0.0, step=5000.0)
prazo = st.text_input("Prazo desejado para conclusão da obra (meses ou data)")

st.header("2️⃣ Características do Terreno")
area_terreno = st.number_input("Área total do terreno (m²)", min_value=1.0)
topografia = st.selectbox("Topografia", ["Plana", "Leve aclive", "Leve declive", "Acentuado declive"])
solo = st.selectbox("Há sondagem disponível?", ["Sim", "Não"])
acesso = st.selectbox("Rua pavimentada e redes instaladas?", ["Sim", "Não", "Parcial"])
vegetacao = st.text_input("Vegetação ou interferências (ex: árvores, rochas)")

st.header("3️⃣ Diretrizes Legais")
zoneamento = st.text_input("Zoneamento (ex: ZR1, ZR2...)")
recuos = st.text_input("Recuos conhecidos (frontal, lateral, fundo)")
gabarito = st.text_input("Altura máxima permitida (em metros/pavimentos)")
aprovacao = st.selectbox("Projeto já protocolado na prefeitura?", ["Não", "Sim, em andamento", "Sim, aprovado"])

st.header("4️⃣ Programa de Necessidades")
tipo_residencia = st.selectbox("Tipo de residência", ["Térrea", "Sobrado", "Com subsolo"])
quartos = st.number_input("Número de quartos", min_value=1, step=1)
banheiros = st.number_input("Número de banheiros", min_value=1, step=1)
garagem = st.number_input("Vagas de garagem", min_value=0, step=1)
area_construida = st.number_input("Área construída desejada (m²)", min_value=30.0)
sustentavel = st.selectbox("Deseja soluções sustentáveis?", ["Sim", "Não"])
ampliacao = st.selectbox("Prevê ampliação futura?", ["Sim", "Não"])

st.header("5️⃣ Sistema Construtivo e Acabamento")
sistema = st.selectbox("Preferência de sistema construtivo", 
                       ["Indefinido", "Alvenaria convencional", "Steel Frame", "Wood Frame", "Concreto pré-moldado"])
acabamento = st.selectbox("Padrão de acabamento desejado", ["Baixo", "Médio", "Alto"])
fornecedores = st.text_input("Há construtora/empreiteiro definido?")

st.header("6️⃣ Custos e Financiamento")
forma_pagamento = st.selectbox("Forma de pagamento", ["Recursos próprios", "Financiamento", "Autoconstrução"])
reserva = st.selectbox("Possui reserva para imprevistos (~10%)?", ["Sim", "Não"])
custos_extra = st.multiselect("Custos previstos", ["Projetos complementares", "Taxas de aprovação", "ART/RRT", "Nenhum"])

st.header("7️⃣ Expectativas e Prioridades")
prioridade = st.selectbox("O que é mais importante?", ["Custo", "Prazo", "Conforto", "Estética"])
flexibilidade = st.selectbox("Aceitam adaptações conforme viabilidade?", ["Sim", "Não"])
observacoes = st.text_area("Observações adicionais")

# Botão final
if st.button("📄 Gerar resumo"):
    dados = {
        "Cliente": proprietarios,
        "Endereço": endereco,
        "Objetivo": objetivo,
        "Orçamento": orcamento,
        "Prazo": prazo,
        "Terreno": {
            "Área (m²)": area_terreno,
            "Topografia": topografia,
            "Sondagem": solo,
            "Acesso": acesso,
            "Vegetação": vegetacao
        },
        "Legislação": {
            "Zoneamento": zoneamento,
            "Recuos": recuos,
            "Gabarito": gabarito,
            "Aprovação": aprovacao
        },
        "Programa": {
            "Tipo": tipo_residencia,
            "Quartos": quartos,
            "Banheiros": banheiros,
            "Garagem": garagem,
            "Área construída": area_construida,
            "Sustentável": sustentável,
            "Ampliação futura": ampliacao
        },
        "Construção": {
            "Sistema": sistema,
            "Acabamento": acabamento,
            "Fornecedor": fornecedores
        },
        "Financeiro": {
            "Forma de pagamento": forma_pagamento,
            "Reserva": reserva,
            "Custos extras": custos_extra
        },
        "Expectativas": {
            "Prioridade": prioridade,
            "Flexibilidade": flexibilidade,
            "Observações": observacoes
        }
    }

    st.success("✅ Questionário concluído!")
    st.subheader("Resumo das respostas:")
    st.json(dados)

    # Exporta JSON
    json_str = json.dumps(dados, indent=4, ensure_ascii=False)
    st.download_button(
        label="⬇️ Baixar respostas em JSON",
        data=json_str,
        file_name="viabilidade_respostas.json",
        mime="application/json"
    )
