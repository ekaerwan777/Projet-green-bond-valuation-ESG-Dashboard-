import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Dashboard Climat & ESG")

st.write("Analyse des indicateurs climatiques, sociaux et de gouvernance.")

# MENU
section = st.sidebar.selectbox(
    "Choisir une section",
    ["Température mondiale", "Niveau de la mer", "CO2 par pays", "CO2 par entreprise", "Égalité salariale"]
)

# ==============================
# TEMPERATURE
# ==============================

if section == "Température mondiale":

    df_temp = pd.read_csv("Temperature.csv")

    fig = px.line(
        df_temp,
        x="Year",
        y="Temperature",
        title="Evolution de la température moyenne mondiale"
    )
    
    st.plotly_chart(fig)
    
    st.write(""" Les données montrent une augmentation progressive des anomalies de température 
             depuis le début du XXe siècle, avec une accélération significative 
             après les années 1980, confirmant le réchauffement climatique global.
             """)


# ==============================
# SEA LEVEL
# ==============================

elif section == "Niveau de la mer":

    df_sea = pd.read_csv("Sea_level.csv")

    fig = px.line(
        df_sea,
        x="year",
        y="SeaLevel",
        title="Evolution du niveau moyen des océans"
    )

    df_sea["Diff"] = df_sea["SeaLevel"].diff()
    kpi = df_sea["Diff"].dropna().mean()
    st.metric(
    "Augmentation moyenne annuelle (mm)",
    f"{round(kpi, 2)} mm/an"
)

    st.plotly_chart(fig)

    st.markdown("""
                Les données montrent l’évolution du niveau moyen global des océans mesuré par satellites.
                Les valeurs négatives ou positives représentent un écart par rapport à une référence historique.
                
                L’augmentation observée au fil des années constitue un indicateur majeur du changement climatique,
                lié à la fonte des calottes glaciaires et à la dilatation thermique des eaux océaniques.
                """)

# ==============================
# CO2 PAR PAYS
# ==============================

elif section == "CO2 par pays":

    df_CO2_Country = pd.read_csv("co2_countries.csv")

    top = df_CO2_Country.sort_values("CO2", ascending=False).head(10)

    fig = px.bar(
        top,
        x="Year",
        y="CO2",
        title="Top 10 des pays émetteurs de CO2 (2020)"
    )
    

    st.plotly_chart(fig)
    
    st.markdown("""Les données représentent les émissions annuelles de CO₂ pour les pays sélectionnés.
                
                L’axe horizontal (Year) indique l’année de mesure, tandis que l’axe vertical (CO2) correspond aux émissions exprimées
                en millions de tonnes de CO₂ équivalent.
                
                Ce graphique permet d’analyser l’évolution temporelle des émissions
                et d’identifier les pays dont l’impact environnemental est le plus élevé.
                """)

# ==============================
# CO2 ENTREPRISES
# ==============================

elif section == "CO2 par entreprise":

    df_CO2_companies = pd.read_csv("co2_companies.csv")
    year_selected = st.slider(
    "Choisir une année",
    int(df_CO2_companies["year"].min()),
    int(df_CO2_companies["year"].max()),
    2020
    )
    df_year = df_CO2_companies[df_CO2_companies["year"] == year_selected]

    # Top 10 entreprises polluantes
    top10 = df_year.sort_values("CO2", ascending=False).head(10)

    fig = px.bar(
        top10,
        x="Company",
        y="CO2",
        title=f"Entreprises les plus émettrices ({year_selected})"
    )
    

    st.plotly_chart(fig)
    
    st.markdown(""" Ce graphique présente le classement des entreprises ayant
                les émissions de CO₂ les plus élevées pour une année donnée.
                
                Il permet d’identifier les principaux contributeurs industriels
                aux émissions de gaz à effet de serre.
                """)

# ==============================
# EGALITE SALARIALE
# ==============================

elif section == "Égalité salariale":

    df_equity = pd.read_csv("gender.csv")
    
    country = st.selectbox("Choisir un pays", df_equity["Country"].unique())

    df_country = df_equity[df_equity["Country"] == country]
    
    fig = px.line(df_country, x="Year", y="Value")
    
    st.plotly_chart(fig)

    st.markdown("""
                Les données proviennent d’Eurostat et mesurent les indicateurs du marché du travail  et des conditions sociales selon les pays et les années.
                
                L’axe horizontal représente l’année d’observation,  tandis que l’axe vertical correspond à la valeur de l’indicateur sélectionné.
                
                Cet indicateur permet d’analyser l’évolution des conditions d’emploi, de participation au marché du travail ou d’inégalités sociales selon le pays choisi.
                """)
