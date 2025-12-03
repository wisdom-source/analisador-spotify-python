import pandas as pd
import plotly.express as px
def carregar_dados():
    try:
        df = pd.read_csv('spotify_analysis_dataset.csv')
        return df
    except FileNotFoundError:
        print('O arquivo não foi encontrado ou a integridade foi comprometida')
        return None

def analise_basica(df):
    if df is None:
        print("Nenhum dado para analisar.")
        return
    dp = df['tempo'].std()
    dp2 = df['popularity'].std()
    print("Análise Básica dos Dados:")
    print(df.head())
    print(df.info())
    print(df.describe())
    print(f"Desvio Padrão da coluna 'tempo': {dp}")
    print(f"Desvio Padrão da coluna 'popularity': {dp2}")
    m = df['tempo'].median()
    m2 = df['popularity'].median()
    print(m)
    print(m2)
    
def analise_avançada(df):
    if df is None:
        print("Nenhum dado para analisar.")
        return
    print("Análise Avançada dos Dados:")
    try:
        a = df.groupby('danceability')['popularity'].mean().sort_values(ascending=False).head(10)
        m = df['tempo'].median()
        m2 = df['popularity'].median()
        print(f'top dez musicas mais dançantes:\n{a}')
    except KeyError as e:
        print(f"Coluna não encontrada: {e}")
def grafico(df):
    if df is None:
        print('Nenhum dado para analisar.')
        return
    df = df[df['tempo']>90]
    df = df[df['popularity']>70]
    px.bar(df, x='tempo', y='popularity', title='Relação entre tempo e popularidade').show()
def main():
    df_principal = carregar_dados()
    if df_principal is not None:
        analise_basica(df_principal)
        analise_avançada(df_principal)
        grafico(df_principal)
    print("Análise concluída.")
if __name__ == "__main__":
    main()