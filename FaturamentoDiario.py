import json

# Lendo os dados de faturamento diário de um arquivo JSON
with open("dados.json"  , encoding='utf-8') as meu_jason:
   dados = json.load(meu_jason)


print
('==========>==========>==========>==========>==========>==========>==========>==========>==========>')

valores = [] # lista para armazenar os valores

for i in dados:
   if i['valor'] != 0.0: # verifique se o valor é diferente de 0.0
      valores.append(i['valor']) # adicione o valor à lista

menor_valor = min(valores) # encontre o menor valor na lista

# Imprimindo o valor do dia que teve menor faturamento. 
print("O menor valor de faturamento ocorrido em um dia do mês foi:", menor_valor)

print('==========>==========>==========>==========>==========>==========>==========>==========>==========>')

valores = [dia['valor'] for dia in dados]

# Obtendo o valor mínimo
valor_maximo = max(valores)

# Imprimindo o valor do dia que teve maior faturamento. 
print('O  valor de faturamento ocorrido em um dia do mês foi::', valor_maximo)

print('==========>==========>==========>==========>==========>==========>==========>==========>==========>')

valores = [dia['valor'] for dia in dados]

# Calculando a média mensal de faturamento diário
media_mensal = sum(valores) / len(valores)

# Contando quantos dias tiveram um valor de faturamento diário maior que a média mensal
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

# Imprimindo o resultado
print("O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi:", 
dias_acima_da_media)

print('==========>==========>==========>==========>==========>==========>==========>==========>==========>')
