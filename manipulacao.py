import streamlit as st
import pandas as pd
import io 
import locale 

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    try:
        
        locale.setlocale(locale.LC_ALL, 'pt_BR')
    except locale.Error:
    
        st.warning("Não foi possível configurar o formato de número (locale).")


st.set_page_config(page_title="Análise de Dados - Base", layout="wide")

# CSS 
st.markdown("""
    <style>
        .titulo-esquerda {
            text-align: left !important;
            padding-left: 10px;
        }
    </style>
""", unsafe_allow_html=True)


# ---- TÍTULO ----
st.markdown(
    """
    <h1 class='titulo-esquerda'>
        📊 Análise de Dados - Base
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("Faça upload de um arquivo CSV ou Excel para visualizar a análise automática.")

# ---- UPLOAD ----
arquivo = st.file_uploader("Selecione o arquivo", type=["csv", "xlsx"])

if arquivo:

    if arquivo.name.endswith(".csv"):
        df = pd.read_csv(arquivo)
    else:
        df = pd.read_excel(arquivo)


    st.subheader("📄 DataFrame Carregado")
    st.dataframe(df)

    df_convertido = df.copy()

    st.subheader("📌 Linhas Duplicadas")
    duplicados = df[df.duplicated()]

    st.write(duplicados)
    st.write(f"Total de duplicados: {duplicados.shape[0]}")

    st.subheader("❗ Quantidade de Valores Nulos por Coluna")
    st.write(df.isnull().sum())

    st.subheader("📌 Tipos de Dados das Colunas")
    st.write(df.dtypes)

    st.subheader("📈 Estatísticas Descritivas")
    st.write(df.describe().round(2))


# ===== RANKING DAS MAIORES COLUNAS NUMÉRICAS =====
    st.subheader("📊 Ranking das Colunas Numéricas")

# Seleciona apenas colunas numéricas
    num_cols = df.select_dtypes(include="number")

    if num_cols.shape[1] == 0:
        st.info("⚠ A base não possui colunas numéricas para gerar ranking.")
    else:
        
        formato_pt_br = lambda x: locale.format_string("%.2f", x, grouping=True)
        
        st.markdown("### 🏆 Top 5 🥇 Maior Soma")
        soma_rank = num_cols.sum().sort_values(ascending=False).head(5)

    
        st.dataframe(soma_rank.to_frame().T.style.format(formato_pt_br))

    

        st.markdown("### 🏆 Top 5 🥈 Maior Média")
        media_rank = num_cols.mean().sort_values(ascending=False).head(5)

        st.dataframe(media_rank.to_frame().T.style.format(formato_pt_br))

else:
    st.info("⬆ Faça upload de um arquivo para começar.")