faturamento = {
    'SP': 'R$67.836,43',
    'RJ': 'R$36.678,66',
    'MG': 'R$29.229,88',
    'ES': 'R$27.165,48',
    'Outros': 'R$19.849,53'
}

def converter_valor(valor_str):
    valor_str = valor_str.replace('R$', '').strip()  
    parte_inteira, parte_decimal = valor_str.split(',') 
    parte_inteira = parte_inteira.replace('.', '') 
    return float(f"{parte_inteira}.{parte_decimal}")  

valores_convertidos = {estado: converter_valor(v) for estado, v in faturamento.items()}
total = sum(valores_convertidos.values())

percentuais = {estado: (valor / total) * 100 for estado, valor in valores_convertidos.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")