
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set page config for theme and layout
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Análise de Impacto dos Jogos",
    page_icon="🎮"
)

# Custom CSS for blue theme and pink details
st.markdown("""
<style>
.stApp {
    background-color: #E0F2F7; /* Light Blue Background */
    color: #001F3F; /* Dark Blue Text */
}
/* Adjusting sidebar background and text */
.st-emotion-cache-vk32z9 {
    background-color: #ADD8E6; /* Lighter Blue for sidebar */
    color: #001F3F;
}
.st-emotion-cache-1ym393r {
    color: #001F3F;
}
.st-emotion-cache-k7v3kt {
    color: #000080; /* Navy Blue for titles */
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: #000080; /* Navy Blue for headers */
}

/* Buttons with a pink accent */
.stButton>button {
    background-color: #FF69B4; /* Hot Pink */
    color: white;
    border-radius: 5px;
    border: none;
    padding: 10px 20px;
}
.stButton>button:hover {
    background-color: #FF1493; /* Deep Pink on hover */
    color: white;
}

/* Streamlit elements for better visual separation */
.st-emotion-cache-16cq8s4 {
    background-color: #FFFFFF; /* White for content blocks */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)


st.title('Análise do Impacto dos Jogos nas Notas Acadêmicas')

# Load data
df = pd.read_csv("Gaming_Academic_Performance.csv")

# Rename columns
df = df.rename(columns={
    'student_id': 'ID_Aluno',
    'age': 'Idade',
    'gender': 'Gênero',
    'gaming_hours': 'Horas_de_Jogo',
    'study_hours': 'Horas_de_Estudo',
    'sleep_hours': 'Horas_de_Sono',
    'attendance': 'Frequência',
    'gaming_genre': 'Gênero_de_Jogo',
    'social_activity': 'Atividade_Social',
    'device_usage': 'Uso_de_Dispositivo',
    'reaction_time_ms': 'Tempo_de_Reação_ms',
    'addiction_score': 'Pontuação_de_Vício',
    'stress_level': 'Nível_de_Estresse',
    'grades': 'Notas'
})

st.subheader('Visão Geral dos Dados')
st.write(df.head())

# --- Sidebar for analysis selection ---
st.sidebar.title('Opções de Análise')
analysis_options = [
    'Horas de Uso de Dispositivos e Nível de Estresse',
    'Média de Notas por Categoria de Horas de Estudo',
    'Média de Notas por Categoria de Horas de Jogo',
    'Média de Notas por Categoria de Horas de Sono'
]
chosen_analysis = st.sidebar.selectbox('Escolha a Análise para Visualizar:', analysis_options)


# Plot 1: Horas de uso de dispositivos e nível de estresse
if chosen_analysis == 'Horas de Uso de Dispositivos e Nível de Estresse':
    st.subheader('Horas de Uso de Dispositivos e Nível de Estresse')
    # Criar faixas de horas de uso
    df['faixa_uso'] = pd.cut(
      df['Uso_de_Dispositivo'],
      bins=[0, 2, 4, 6, 9, 12],
      labels=['0-2h', '2-4h', '4-6h', '6-8h', '8h+']
    )
    # Mapear os níveis de estresse para valores numéricos
    stress_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    df['stress_level_numeric'] = df['Nível_de_Estresse'].map(stress_mapping)
    # Média do estresse por faixa
    dados = df.groupby('faixa_uso', observed=True)['stress_level_numeric'].mean()

    fig1, ax1 = plt.subplots(figsize=(10,6)) # Increased figure size for better display
    dados.plot(kind='bar', color=['#80B1D3', '#FB8072', '#B3DE69', '#FCCDE5', '#BEBADA'], ax=ax1) # Changed colors to fit theme
    ax1.set_title('Horas de uso de dispositivos e nível de estresse')
    ax1.set_xlabel('Faixa de horas de uso')
    ax1.set_ylabel('Nível médio de estresse')
    ax1.tick_params(axis='x', rotation=45) # Rotated for better label readability
    plt.tight_layout()
    st.pyplot(fig1)

# Plot 2: Média de Notas por Categoria de Horas de Estudo
if chosen_analysis == 'Média de Notas por Categoria de Horas de Estudo':
    st.subheader('Média de Notas por Categoria de Horas de Estudo')
    study_hours_bins = [0, 2, 4, 6, 8, np.inf]
    study_hours_labels = ['0-2 horas', '2-4 horas', '4-6 horas', '6-8 horas', '8+ horas']
    df['study_hours_category'] = pd.cut(df['Horas_de_Estudo'], bins=study_hours_bins, labels=study_hours_labels, right=False)
    average_grades_by_study = df.groupby('study_hours_category', observed=False)['Notas'].mean().reset_index()

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=average_grades_by_study, x='study_hours_category', y='Notas', marker='o', color='#377EB8', ax=ax2) # Blue color
    ax2.set_title('Média de Notas por Categoria de Horas de Estudo')
    ax2.set_xlabel('Horas de Estudo')
    ax2.set_ylabel('Média de Notas')
    ax2.grid(True, linestyle='--', alpha=0.7) # Added grid back for readability
    ax2.tick_params(axis='x', rotation=45) # Removed ha='right', adjusted rotation for display
    plt.tight_layout()
    st.pyplot(fig2)

# Plot 3: Média de Notas por Categoria de Horas de Jogo
if chosen_analysis == 'Média de Notas por Categoria de Horas de Jogo':
    st.subheader('Média de Notas por Categoria de Horas de Jogo')
    gaming_hours_bins = [0, 2, 4, 6, 8, np.inf]
    gaming_hours_labels = ['0-2 horas', '2-4 horas', '4-6 horas', '6-8 horas', '8+ horas']
    df['gaming_hours_category'] = pd.cut(df['Horas_de_Jogo'], bins=gaming_hours_bins, labels=gaming_hours_labels, right=False)
    average_grades_by_gaming = df.groupby('gaming_hours_category', observed=False)['Notas'].mean().reset_index()

    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=average_grades_by_gaming, x='gaming_hours_category', y='Notas', marker='o', color='#E41A1C', ax=ax3) # Red/Pinkish color for contrast
    ax3.set_title('Média de Notas por Categoria de Horas de Jogo')
    ax3.set_xlabel('Horas de Jogo')
    ax3.set_ylabel('Média de Notas')
    ax3.grid(True, linestyle='--', alpha=0.7) # Added grid back for readability
    ax3.tick_params(axis='x', rotation=45) # Removed ha='right', adjusted rotation for display
    plt.tight_layout()
    st.pyplot(fig3)

# Plot 4: Média de Notas por Categoria de Horas de Sono
if chosen_analysis == 'Média de Notas por Categoria de Horas de Sono':
    st.subheader('Média de Notas por Categoria de Horas de Sono')
    bins = [4, 5, 6, 7, 8, np.inf]
    labels = ['4-5 horas', '5-6 horas', '6-7 horas', '7-8 horas', '8+ horas']
    df['Categoria_Sono'] = pd.cut(
        df['Horas_de_Sono'],
        bins=bins,
        labels=labels,
        right=False
    )
    media_notas = (
        df.groupby('Categoria_Sono', observed=True)['Notas']
        .mean()
        .reset_index()
    )

    fig4, ax4 = plt.subplots(figsize=(10,6)) # Increased figure size
    sns.barplot(
        data=media_notas,
        x='Categoria_Sono',
        y='Notas',
        hue='Categoria_Sono',
        palette='GnBu', # Green-Blue palette for blue theme
        legend=False,
        ax=ax4
    )
    ax4.set_title('Média de Notas por Categoria de Horas de Sono')
    ax4.set_xlabel('Horas de Sono')
    ax4.set_ylabel('Média de Notas')
    ax4.grid(axis='y', linestyle='--', alpha=0.7) # Added horizontal grid
    ax4.tick_params(axis='x', rotation=0) # Kept rotation 0 for clarity
    plt.tight_layout()
    st.pyplot(fig4)
