import pandas as pd
from tabulate import tabulate  # Importando a biblioteca tabulate

# Definindo as variáveis para cada voo
voo_1 = {
    'Número do voo': '9164',
    'Hora do voo': '03:20',
    'Apenas milhas': 118000,
    'Milhas + dinheiro': {
        'Milhas': 11800,
        'Dinheiro': 1732.00
    },
    'Apenas dinheiro': 2339.45,
    'Escala': 'Direto'
}

voo_2 = {
    'Número do voo': '2613',
    'Hora do voo': '06:20',
    'Apenas milhas': 92000,
    'Milhas + dinheiro': {
        'Milhas': 9200,
        'Dinheiro': 1343.00
    },
    'Apenas dinheiro': 1699.46,
    'Escala': 'Direto'
}

voo_3 = {
    'Número do voo': '2778',
    'Hora do voo': '10:10',
    'Apenas milhas': 124000,
    'Milhas + dinheiro': {
        'Milhas': 12400,
        'Dinheiro': 1818.00
    },
    'Apenas dinheiro': 2450.63,
    'Escala': 'Direto'
}

voo_4 = {
    'Número do voo': '4849',
    'Hora do voo': '14:20',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 3035.00
    },
    'Apenas dinheiro': 3689.46,
    'Escala': 'Direto'
}

voo_5 = {
    'Número do voo': '2808',
    'Hora do voo': '18:50',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 3061.00
    },
    'Apenas dinheiro': 3720.46,
    'Escala': 'Direto'
}

voo_6 = {
    'Número do voo': '4368',
    'Hora do voo': '23:40',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 3035.00
    },
    'Apenas dinheiro': 3689.46,
    'Escala': 'Direto'
}

voo_7 = {
    'Número do voo': '2621',
    'Hora do voo': '09:25',
    'Apenas milhas': 102000,
    'Milhas + dinheiro': {
        'Milhas': 15300,
        'Dinheiro': 1892.00
    },
    'Apenas dinheiro': 2545.46,
    'Escala': 'Com Escala'
}

voo_8 = {
    'Número do voo': '2784',
    'Hora do voo': '13:10',
    'Apenas milhas': 92000,
    'Milhas + dinheiro': {
        'Milhas': 13800,
        'Dinheiro': 1892.00
    },
    'Apenas dinheiro': 2345.46,
    'Escala': 'Com Escala'
}

# Criando uma lista de voos com o objeto correspondente
voos = [
    {'Objeto': 'voo_1', **voo_1},
    {'Objeto': 'voo_2', **voo_2},
    {'Objeto': 'voo_3', **voo_3},
    {'Objeto': 'voo_4', **voo_4},
    {'Objeto': 'voo_5', **voo_5},
    {'Objeto': 'voo_6', **voo_6},
    {'Objeto': 'voo_7', **voo_7},
    {'Objeto': 'voo_8', **voo_8},
]

# Transformando a lista de voos em um DataFrame
df = pd.DataFrame(voos)

# Extraindo as milhas e dinheiro do campo 'Milhas + dinheiro' e criando colunas separadas
df['Milhas'] = df['Milhas + dinheiro'].apply(lambda x: x['Milhas'])
df['Dinheiro'] = df['Milhas + dinheiro'].apply(lambda x: x['Dinheiro'])

# Cálculo para Apenas Milhas vezes Apenas Dinheiro
df['Apenas Milhas x Apenas Dinheiro'] = df['Apenas milhas'] * df['Apenas dinheiro']

# Ordenando pelo cálculo de Apenas Milhas x Apenas Dinheiro
df_sorted_milhas = df.sort_values(by='Apenas Milhas x Apenas Dinheiro')

# Cálculo para (Milhas + Dinheiro) vezes Apenas Dinheiro
df['Milhas+Dinheiro x Apenas Dinheiro'] = (df['Milhas'] + df['Dinheiro']) * df['Apenas dinheiro']

# Ordenando pelo cálculo de (Milhas + Dinheiro) x Apenas Dinheiro
df_sorted_combined = df.sort_values(by='Milhas+Dinheiro x Apenas Dinheiro')

# Função para formatar valores
def formatar_dinheiro(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

def formatar_milhas(valor):
    return f'{valor:,}'.replace(',', '.')

def formatar_porcentagem(valor):
    return f'{valor:,.1f}%'.replace(',', 'X').replace('.', ',').replace('X', '.')

# Aplicando as formatações
df_sorted_milhas['Apenas dinheiro'] = df_sorted_milhas['Apenas dinheiro'].apply(formatar_dinheiro)
df_sorted_milhas['Apenas milhas'] = df_sorted_milhas['Apenas milhas'].apply(formatar_milhas)

# Cálculo da porcentagem de aumento em relação ao menor valor em 'Apenas dinheiro'
menor_valor = df_sorted_milhas['Apenas dinheiro'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float).min()
df_sorted_milhas['% de Aumento'] = ((df_sorted_milhas['Apenas dinheiro'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float) - menor_valor) / menor_valor * 100).round(1)
df_sorted_milhas['% de Aumento'] = df_sorted_milhas['% de Aumento'].apply(formatar_porcentagem)

# Formatação para a tabela ordenada por (Milhas + Dinheiro) x Apenas Dinheiro
df_sorted_combined['Milhas + dinheiro'] = df_sorted_combined['Milhas + dinheiro'].apply(
    lambda x: f"Milhas: {formatar_milhas(x['Milhas'])}, R$: {formatar_dinheiro(x['Dinheiro']).replace('R$ ', '')}"
)
df_sorted_combined['Apenas dinheiro'] = df_sorted_combined['Apenas dinheiro'].apply(formatar_dinheiro)

# Cálculo da porcentagem de aumento em relação ao menor valor em 'Apenas dinheiro' para a segunda parte
menor_valor_combined = df_sorted_combined['Apenas dinheiro'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float).min()
df_sorted_combined['% de Aumento'] = ((df_sorted_combined['Apenas dinheiro'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float) - menor_valor_combined) / menor_valor_combined * 100).round(1)
df_sorted_combined['% de Aumento'] = df_sorted_combined['% de Aumento'].apply(formatar_porcentagem)

# Ordenando os DataFrames pelas colunas de "Apenas dinheiro"
df_sorted_milhas = df_sorted_milhas.sort_values(by='Apenas dinheiro', key=lambda x: x.str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float))
df_sorted_combined = df_sorted_combined.sort_values(by='Apenas dinheiro', key=lambda x: x.str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float))

# Exibir os resultados com tabulate
print("Ordenado por Apenas Milhas x Apenas Dinheiro, em ordem crescente de preço:")
print(tabulate(df_sorted_milhas[['Objeto', 'Número do voo', 'Hora do voo', 'Apenas milhas', 'Apenas dinheiro', '% de Aumento', 'Escala']],
                headers='keys', tablefmt='pretty', showindex=False))

print("\nOrdenado por (Milhas + Dinheiro), em ordem crescente de preço:")
print(tabulate(df_sorted_combined[['Objeto', 'Número do voo', 'Hora do voo', 'Milhas + dinheiro', 'Apenas dinheiro', '% de Aumento', 'Escala']],
                headers='keys', tablefmt='pretty', showindex=False))
