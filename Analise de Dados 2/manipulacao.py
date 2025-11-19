#Importando as Bibliotecas

import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

#Puxando a Base de Dados

base = pd.read_csv('Vendas.csv')
print('====== Data Frame ======')
print(base, '\n')

print('======== Verficando Valores Nulos ======== \n')
nulo = base.isnull().sum()
print(nulo , '\n')


print('======== Descrição da Tabela ======== \n')

descrever = base.describe().round(2)
print(descrever)


soma_total_por_estado = base.groupby('estado')['valor_total'].sum()
soma_total_por_estado_formatada = soma_total_por_estado.round(1)
soma_total_por_estado_ordenada = soma_total_por_estado_formatada.sort_values(ascending=False)

print('\n======== Soma Total de Vendas por Estado (Arredondada) ========')
print(soma_total_por_estado_ordenada)