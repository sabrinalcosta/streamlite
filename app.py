
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title('Análise do Impacto dos Hábitos de Vida nas Notas Acadêmicas')

# Load data
df = pd.read_csv('Gaming_Academic_Performance.csv')

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

# Plot 1: Horas de uso de dispositivos e nível de estresse
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

fig1, ax1 = plt.subplots(figsize=(7,4))
dados.plot(kind='bar', color=['rosybrown', 'palevioletred', 'plum', 'mediumorchid', 'purple'], ax=ax1)
ax1.set_title('Horas de uso de dispositivos e nível de estresse')
ax1.set_xlabel('Faixa de horas de uso')
ax1.set_ylabel('Nível médio de estresse')
ax1.tick_params(axis='x', rotation=0)
st.pyplot(fig1)

# Plot 2: Média de Notas por Categoria de Horas de Estudo
st.subheader('Média de Notas por Categoria de Horas de Estudo')
study_hours_bins = [0, 2, 4, 6, 8, np.inf]
study_hours_labels = ['0-2 horas', '2-4 horas', '4-6 horas', '6-8 horas', '8+ horas']
df['study_hours_category'] = pd.cut(df['Horas_de_Estudo'], bins=study_hours_bins, labels=study_hours_labels, right=False)
average_grades_by_study = df.groupby('study_hours_category', observed=False)['Notas'].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=average_grades_by_study, x='study_hours_category', y='Notas', marker='o', color='green', ax=ax2)
ax2.set_title('Média de Notas por Categoria de Horas de Estudo')
ax2.set_xlabel('Horas de Estudo')
ax2.set_ylabel('Média de Notas')
ax2.grid(False)
ax2.tick_params(axis='x', rotation=0)
plt.tight_layout()
st.pyplot(fig2)

# Plot 3: Média de Notas por Categoria de Horas de Jogo
st.subheader('Média de Notas por Categoria de Horas de Jogo')
gaming_hours_bins = [0, 2, 4, 6, 8, np.inf]
gaming_hours_labels = ['0-2 horas', '2-4 horas', '4-6 horas', '6-8 horas', '8+ horas']
df['gaming_hours_category'] = pd.cut(df['Horas_de_Jogo'], bins=gaming_hours_bins, labels=gaming_hours_labels, right=False)
average_grades_by_gaming = df.groupby('gaming_hours_category', observed=False)['Notas'].mean().reset_index()

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=average_grades_by_gaming, x='gaming_hours_category', y='Notas', marker='o', color='red', ax=ax3)
ax3.set_title('Média de Notas por Categoria de Horas de Jogo')
ax3.set_xlabel('Horas de Jogo')
ax3.set_ylabel('Média de Notas')
ax3.grid(False)
ax3.tick_params(axis='x', rotation=0)
plt.tight_layout()
st.pyplot(fig3)

# Plot 4: Média de Notas por Categoria de Horas de Sono
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

fig4, ax4 = plt.subplots(figsize=(8,5))
sns.barplot(
    data=media_notas,
    x='Categoria_Sono',
    y='Notas',
    hue='Categoria_Sono',
    palette='rocket',
    legend=False,
    ax=ax4
)
ax4.set_title('Média de Notas por Categoria de Horas de Sono')
ax4.set_xlabel('Horas de Sono')
ax4.set_ylabel('Média de Notas')
ax4.grid(False)
plt.tight_layout()
st.pyplot(fig4)
