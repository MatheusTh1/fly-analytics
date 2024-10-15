import pandas as pd

# Definindo as variáveis para cada voo
voo_1 = {
    'Hora do voo': '03:20',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 1887.00
    },
    'Apenas dinheiro': 2156.46
}

voo_2 = {
    'Hora do voo': '06:20',
    'Apenas milhas': 92000,
    'Milhas + dinheiro': {
        'Milhas': 9200,
        'Dinheiro': 1343.00
    },
    'Apenas dinheiro': 1699.46
}

voo_3 = {
    'Hora do voo': '10:10',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 1982.00
    },
    'Apenas dinheiro': 2258.46
}

voo_4 = {
    'Hora do voo': '14:20',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 3035.00
    },
    'Apenas dinheiro': 3689.46
}

voo_5 = {
    'Hora do voo': '18:50',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 3061.00
    },
    'Apenas dinheiro': 3720.46
}

voo_6 = {
    'Hora do voo': '23:40',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 3035.00
    },
    'Apenas dinheiro': 3689.46
}

voo_7 = {
    'Hora do voo': '09:25',
    'Apenas milhas': 102000,
    'Milhas + dinheiro': {
        'Milhas': 15300,
        'Dinheiro': 2062.00
    },
    'Apenas dinheiro': 2345.46
}

voo_8 = {
    'Hora do voo': '13:10',
    'Apenas milhas': 92000,
    'Milhas + dinheiro': {
        'Milhas': 13800,
        'Dinheiro': 1892.00
    },
    'Apenas dinheiro': 2345.46
}

# Criando uma lista de voos
voos = [voo_1, voo_2, voo_3, voo_4, voo_5, voo_6, voo_7, voo_8]

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
df_sorted_milhas['Apenas milhas'] = df_sorted_milhas['Apenas milhas'].apply(formatar_milhas)  # Formatação de milhas

# Cálculo da porcentagem de aumento em relação ao menor valor em 'Apenas dinheiro'
menor_valor = df_sorted_milhas['Apenas dinheiro'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float).min()
df_sorted_milhas['% de Aumento'] = ((df_sorted_milhas['Apenas dinheiro'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float) - menor_valor) / menor_valor * 100).round(1)
df_sorted_milhas['% de Aumento'] = df_sorted_milhas['% de Aumento'].apply(formatar_porcentagem)

# Formatação para a tabela ordenada por (Milhas + Dinheiro) x Apenas Dinheiro
df_sorted_combined['Milhas + dinheiro'] = df_sorted_combined['Milhas + dinheiro'].apply(
    lambda x: f"Milhas: {formatar_milhas(x['Milhas'])}, Dinheiro: {formatar_dinheiro(x['Dinheiro'])}"
)
df_sorted_combined['Apenas dinheiro'] = df_sorted_combined['Apenas dinheiro'].apply(formatar_dinheiro)

# Cálculo da porcentagem de aumento em relação ao menor valor em 'Apenas dinheiro' para a segunda parte
menor_valor_combined = df_sorted_combined['Apenas dinheiro'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float).min()
df_sorted_combined['% de Aumento'] = ((df_sorted_combined['Apenas dinheiro'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float) - menor_valor_combined) / menor_valor_combined * 100).round(1)
df_sorted_combined['% de Aumento'] = df_sorted_combined['% de Aumento'].apply(formatar_porcentagem)

# Exibir os resultados
print("Ordenado por Apenas Milhas x Apenas Dinheiro:")
print(df_sorted_milhas[['Hora do voo', 'Apenas milhas', 'Apenas dinheiro', '% de Aumento']])  # Incluindo a coluna de % de aumento

print("\nOrdenado por (Milhas + Dinheiro):")
print(df_sorted_combined[['Hora do voo', 'Milhas + dinheiro', 'Apenas dinheiro', '% de Aumento']])
