

import pandas as pd 

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

caminho = r"C:\Users\karen.quiroga\Downloads\python_analise_dados-main\python_analise_dados-main\avengers.csv"
df_01 =pd.read_csv(caminho,encoding='latin1')


### Exibe a quantidade de filmes ( conta distintamente)
qde_filmes = df_01.value_counts("Name/Alias")
### Ao incluir uma lista  no groupby, faz a agragação pela colunas 
qde_filmes_year = df_01.groupby(["Year","Name/Alias"]).size()

print (qde_filmes)
print (qde_filmes_year)
print(df_01.columns) # exive quantidade de colunas
print (df_01.shape) # exibe linhas e coluna

### filtra conforme campo/texto 
mortos = df_01[df_01['Death1'] == 'YES']
print(mortos[['Name/Alias', 'Death1']])

### filtra conforme campo/texto
filmes_2015 = df_01[df_01["Year"] == 2015] ## filtra pela coluna Year e texo 2015
print(filmes_2015[["Year", "Name/Alias" ]]) ## Aqui especifica as colunas

## Ver se há duplicatas no DataFrame inteiro
duplicadas = df_01[df_01.duplicated()]
print(duplicadas)

## Ver duplicadas com base em uma coluna específica
duplicadas_nome = df_01[df_01.duplicated(subset='Name/Alias')]
print(duplicadas_nome)
