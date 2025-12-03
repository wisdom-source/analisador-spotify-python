import pandas as pd
import plotly.express as px
import sys

def carregar_dados():
    """
    Tenta carregar o arquivo CSV. Se houver erro, trata a exceção.
    """
    try:
        df = pd.read_csv('spotify_analysis_dataset.csv')
        return df
    except FileNotFoundError:
        # A forma mais limpa de tratar o erro sem o "as e"
        print('ERRO: O arquivo spotify_analysis_dataset.csv não foi encontrado.')
        print('O programa será encerrado. Verifique o nome do arquivo.')
        return None

def analise_basica(df):
    """
    Realiza a inspeção e calcula as estatísticas descritivas básicas.
    """
    if df is None:
        return
    
    dp = df['tempo'].std()
    dp2 = df['popularity'].std()
    m = df['tempo'].median()
    m2 = df['popularity'].median()
    
    print("\n--- Análise Básica dos Dados ---")
    print(df.head())
    print('\n')
    print(df.info())
    print('\n')
    print(df.describe())
    
    print(f"\nDesvio Padrão da coluna 'tempo': {dp}")
    print(f"Desvio Padrão da coluna 'popularity': {dp2}")
    print(f"Mediana do Tempo (Duração): {m}")
    print(f"Mediana da Popularidade: {m2}")
    
def analise_avancada(df):
    """
    Realiza o agrupamento de dados e gera a visualização principal.
    """
    if df is None:
        return
        
    print("\n--- Análise Avançada: Agrupamento e Visualização ---")
    
    try:
        # 1. Agrupamento: Popularidade média por nível de danceability
        analise_popularidade = df.groupby('danceability')['popularity'].mean().sort_values(ascending=False).head(10)
        
        print(f'\nTop dez médias de Popularidade por Nível de Danceability:\n{analise_popularidade}')

        # 2. Preparação para o Gráfico
        # Converte a Série em DataFrame para o Plotly
        df_plot = analise_popularidade.reset_index() 
        df_plot.columns = ['Danceability', 'Popularidade Média'] 

        # 3. CRIAÇÃO DO GRÁFICO (Armazena em 'fig')
        fig = px.bar(
            df_plot, 
            x='Danceability', 
            y='Popularidade Média',
            title='Popularidade Média por Nível de Danceability (Top 10)',
            color='Popularidade Média'
        )
        
        # 4. Salva o arquivo HTML
        nome_arquivo = 'popularidade_por_danceability.html'
        fig.write_html(nome_arquivo) 
        
        print(f"\nGráfico interativo salvo com sucesso: '{nome_arquivo}'")

    except KeyError as e:
        # Tratamento de erro específico para colunas ausentes
        print(f"AVISO: Coluna necessária para o agrupamento não encontrada: {e}")

def main():
    """Função principal que coordena o fluxo do programa."""
    df_principal = carregar_dados()
    
    if df_principal is not None:
        analise_basica(df_principal)
        analise_avancada(df_principal)
        
    print("\nAnálise concluída.")

if __name__ == "__main__":
    main()
