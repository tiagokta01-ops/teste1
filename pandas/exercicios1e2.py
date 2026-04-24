'''#exercicospandas
#1
Carregando o dataset
df = pd.read_csv('jogos.csv')

print("--- Respostas do Exercício 1 ---")

#a
print(f"a) Quantidade de jogos: {df.shape[0]}")

#b
print("\nb) Tipos de dados:")
print(df.dtypes)

#c
print(f"\nc) Preço médio: R$ {df['preco'].mean():.2f}")
print(f"   Nota média: {df['nota'].mean():.1f}")

#d
print("\nd) Nome e Preço (Top 3):")
print(df[['jogo', 'preco']].head(3))'''


'''#2
import pandas as pd

df = pd.read_csv('jogos.csv')

#1 Contagem por gênero (mais frequente primeiro)
print(df['genero'].value_counts())

#2 Maior nota e menor preço
print(df['nota'].max(), df['preco'].min())

#3 Nome do jogo no índice 5 (rótulo)
print(df.loc[5, 'jogo'])

#4 Linhas 0-2 e colunas 1-2 (posição)
print(df.iloc[0:3, 1:3])

#5 Últimas 3 linhas das colunas jogo e ano
print(df[['jogo', 'ano']].tail(3))

#6 Apenas as médias das colunas numéricas
print(df.describe().loc['mean'])'''
