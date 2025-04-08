import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

valores = [dia['valor'] for dia in dados]

menor = min(valores)
maior = max(valores)

valores_nao_zero = [v for v in valores if v > 0]
soma_nao_zero = sum(valores_nao_zero)
num_dias_nao_zero = len(valores_nao_zero)

media = soma_nao_zero / num_dias_nao_zero if num_dias_nao_zero != 0 else 0

dias_acima_media = sum(1 for dia in dados if dia['valor'] > media)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")