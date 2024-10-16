import pandas as pd
from tabulate import tabulate

# Definindo as variáveis para cada voo com a nova chave 'Data voo'
voo_1 = {
    'Data voo': '26/10/2024',
    'Número do voo': '2613',
    'Hora do voo': '06:15',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 2551.00
    },
    'Apenas dinheiro': 3120.46,
    'Escala': 'Direto'
}

voo_2 = {
    'Data voo': '26/10/2024',
    'Número do voo': '2778',
    'Hora do voo': '10:05',
    'Apenas milhas': 96000,
    'Milhas + dinheiro': {
        'Milhas': 14400,
        'Dinheiro': 1097.00
    },
    'Apenas dinheiro': 1490.46,
    'Escala': 'Direto'
}

voo_3 = {
    'Data voo': '26/10/2024',
    'Número do voo': '2508',
    'Hora do voo': '14:20',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 3061.00
    },
    'Apenas dinheiro': 3720.46,
    'Escala': 'Direto'
}

voo_4 = {
    'Data voo': '26/10/2024',
    'Número do voo': '4918',
    'Hora do voo': '19:15',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 2918.00
    },
    'Apenas dinheiro': 3552.46,
    'Escala': 'Direto'
}

voo_5 = {
    'Data voo': '26/10/2024',
    'Número do voo': '4368',
    'Hora do voo': '23:40',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 2553.00
    },
    'Apenas dinheiro': 3122.46,
    'Escala': 'Direto'
}

voo_6 = {
    'Data voo': '26/10/2024',
    'Número do voo': '4147',
    'Hora do voo': '11:35',
    'Apenas milhas': 116000,
    'Milhas + dinheiro': {
        'Milhas': 13950,
        'Dinheiro': 1643.00
    },
    'Apenas dinheiro': 2226.09,
    'Escala': '1 conexão'
}

# Definindo os voos de 27/12
voo_7 = {
    'Data voo': '27/12/2024',
    'Número do voo': '2613',
    'Hora do voo': '06:15',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 2551.00
    },
    'Apenas dinheiro': 2614.46,
    'Escala': 'Direto'
}

voo_8 = {
    'Data voo': '27/12/2024',
    'Número do voo': '2778',
    'Hora do voo': '10:05',
    'Apenas milhas': 96000,
    'Milhas + dinheiro': {
        'Milhas': 14400,
        'Dinheiro': 1097.00
    },
    'Apenas dinheiro': 1490.46,
    'Escala': 'Direto'
}

voo_9 = {
    'Data voo': '27/12/2024',
    'Número do voo': '4849',
    'Hora do voo': '14:20',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 3061.00
    },
    'Apenas dinheiro': 3861.09,
    'Escala': 'Direto'
}

voo_10 = {
    'Data voo': '27/12/2024',
    'Número do voo': '4918',
    'Hora do voo': '19:15',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 2918.00
    },
    'Apenas dinheiro': 2614.46,
    'Escala': 'Direto'
}

voo_11 = {
    'Data voo': '27/12/2024',
    'Número do voo': '4368',
    'Hora do voo': '23:30',
    'Apenas milhas': 130000,
    'Milhas + dinheiro': {
        'Milhas': 13000,
        'Dinheiro': 2553.00
    },
    'Apenas dinheiro': 3122.46,
    'Escala': 'Direto'
}

voo_12 = {
    'Data voo': '27/12/2024',
    'Número do voo': '4147',
    'Hora do voo': '11:35',
    'Apenas milhas': 116000,
    'Milhas + dinheiro': {
        'Milhas': 13950,
        'Dinheiro': 1643.00
    },
    'Apenas dinheiro': 2855.46,
    'Escala': '1 conexão'
}

# Criando a lista de voos
voos = [
    {'Objeto': 'voo_1', **voo_1},
    {'Objeto': 'voo_2', **voo_2},
    {'Objeto': 'voo_3', **voo_3},
    {'Objeto': 'voo_4', **voo_4},
    {'Objeto': 'voo_5', **voo_5},
    {'Objeto': 'voo_6', **voo_6},
    {'Objeto': 'voo_7', **voo_7},
    {'Objeto': 'voo_8', **voo_8},
    {'Objeto': 'voo_9', **voo_9},
    {'Objeto': 'voo_10', **voo_10},
    {'Objeto': 'voo_11', **voo_11},
    {'Objeto': 'voo_12', **voo_12}
]

# Criando DataFrame
df = pd.DataFrame(voos)

# Variáveis para cálculo de compra de milhas
pontos_disponiveis = 9000  # Alterado para 9000 para testar
custo_ponto = 0.45

# Log dos pontos disponíveis e custo por ponto formatados
pontos_disponiveis_formatado = f"{pontos_disponiveis:,.0f}".replace(',', '.')
custo_ponto_formatado = f"R$ {custo_ponto:,.2f}".replace('.', ',')

print(f"\nPontos disponíveis hoje: {pontos_disponiveis_formatado}")
print(f"Preço de aquisição por 1 milha: {custo_ponto_formatado}\n")

# Função para calcular milhas faltantes e custo
def calcular_milhas_faltantes(pontos_necessarios):
    pontos_faltantes = max(0, pontos_necessarios - pontos_disponiveis)
    custo_completar_milhas = pontos_faltantes * custo_ponto
    return pontos_faltantes, custo_completar_milhas

# -----------------------------------------
# Tabela 1: Apenas Milhas
# -----------------------------------------

# Calculando apenas milhas
df['Milhas faltantes'] = df['Apenas milhas'].apply(lambda x: calcular_milhas_faltantes(x)[0])
df['R$ compra em milhas'] = df['Apenas milhas'].apply(lambda x: calcular_milhas_faltantes(x)[1])
df['Utilizar milhas'] = df['R$ compra em milhas'].apply(lambda x: 'Sim' if x < df['Apenas dinheiro'].min() else 'Não')

# Exibir a primeira tabela: Apenas Milhas
tabela1 = df[['Objeto', 'Data voo', 'Escala', 'Utilizar milhas', 'Número do voo', 'Hora do voo', 'Apenas milhas', 'Apenas dinheiro', 'Milhas faltantes', 'R$ compra em milhas']].copy()

# Formatação dos valores
tabela1['Apenas dinheiro'] = tabela1['Apenas dinheiro'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',', 1).replace('X', '.'))
tabela1['Apenas milhas'] = tabela1['Apenas milhas'].apply(lambda x: f"{x:,.0f}".replace(',', '.'))
tabela1['R$ compra em milhas'] = tabela1['R$ compra em milhas'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',', 1).replace('X', '.'))

# Formatação da coluna de milhas faltantes
tabela1['Milhas faltantes'] = tabela1['Milhas faltantes'].apply(lambda x: f"{x:,.0f}".replace(',', '.'))

# Calcular o menor valor da tabela 1 para o cálculo de aumento
def converter_para_float(x):
    if isinstance(x, str):
        return float(x.replace('R$ ', '').replace('.', '').replace(',', '.'))
    elif isinstance(x, float):
        return x
    else:
        return None

df['Apenas dinheiro'] = df['Apenas dinheiro'].apply(converter_para_float)
menor_valor_tabela1 = df['Apenas dinheiro'].min()

# Adicionar coluna de % de aumento na tabela 1
tabela1['% de aumento'] = ((df['Apenas dinheiro'] - menor_valor_tabela1) / menor_valor_tabela1 * 100).round(1).astype(str) + '%'

# Mover a coluna % de aumento para depois de Apenas dinheiro
tabela1 = tabela1[['Objeto', 'Data voo', 'Escala', 'Utilizar milhas', 'Número do voo', 'Hora do voo', 'Apenas milhas', 'Apenas dinheiro', '% de aumento', 'Milhas faltantes', 'R$ compra em milhas']]

# Ordenar a tabela 1 pelo valor em dinheiro
tabela1 = tabela1.sort_values(by='Apenas dinheiro')

# Exibir resultados da tabela 1
print("Tabela 1: Apenas Dinheiro ou Milhas")
print(tabulate(tabela1, headers='keys', tablefmt='pretty', showindex=False))

# -----------------------------------------
# Tabela 2: Milhas + Dinheiro
# -----------------------------------------

# Função para formatar 'Milhas + dinheiro' corretamente
def formatar_milhas_dinheiro(x):
    return f"{x['Milhas']:,} milhas + R$ {x['Dinheiro']:,.2f}".replace(',', 'X').replace('.', ',', 1).replace('X', '.')

# Aplicar a função de formatação
df['Milhas + dinheiro'] = df['Milhas + dinheiro'].apply(formatar_milhas_dinheiro)

# Calculando milhas faltantes para milhas + dinheiro
df['Milhas faltantes'] = df['Milhas + dinheiro'].apply(lambda x: calcular_milhas_faltantes(int(x.split(' milhas')[0].replace('.', '')))[0])
df['R$ compra em milhas'] = df['Milhas + dinheiro'].apply(lambda x: calcular_milhas_faltantes(int(x.split(' milhas')[0].replace('.', '')))[1])

# Cálculo do Valor Total (somando o valor do dinheiro + o custo das milhas faltantes)
df['Valor Total'] = df['Milhas + dinheiro'].apply(lambda x: float(x.split('+ R$ ')[-1].replace('.', '').replace(',', '.'))) + df['R$ compra em milhas']

# Adicionando a coluna 'Utilizar milhas' à tabela 2
df['Utilizar milhas'] = df.apply(
    lambda row: 'Sim' if (row['R$ compra em milhas'] + float(row['Milhas + dinheiro'].split('+ R$ ')[-1].replace('.', '').replace(',', '.'))) < menor_valor_tabela1 else 'Não',
    axis=1
)

# Corrigindo o cálculo da % de aumento na tabela 2 em relação ao menor valor da tabela 1
df['% de aumento'] = ((df['Valor Total'] - menor_valor_tabela1) / menor_valor_tabela1 * 100).round(1).astype(str) + '%'

# Exibir a segunda tabela: Milhas + Dinheiro
tabela2 = df[['Objeto', 'Data voo', 'Escala', 'Utilizar milhas', 'Número do voo', 'Hora do voo', 'Milhas + dinheiro', '% de aumento', 'Valor Total', 'Milhas faltantes', 'R$ compra em milhas']].copy()

# Formatando as colunas
tabela2['R$ compra em milhas'] = tabela2['R$ compra em milhas'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',', 1).replace('X', '.'))
tabela2['Valor Total'] = tabela2['Valor Total'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',', 1).replace('X', '.'))

# Ordenar a tabela 2 pelo valor total
tabela2 = tabela2.sort_values(by='Valor Total')

# Exibir resultados da tabela 2
print("\nTabela 2: Milhas + Dinheiro")
print(tabulate(tabela2, headers='keys', tablefmt='pretty', showindex=False))
