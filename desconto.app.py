#Desconto progressivo

#Solicita o valor total da compra
valor = float(input("Digite o valor total da compra: R$ "))

#Verifica qual desconto sera aplicado
if valor < 200:
    desconto = 0.05
elif valor < 300:
    desconto = 0.10
else:
    desconto = 0.15

#Calcula o valor do desconto
valor_desconto = valor * desconto

#Calcula o valor final da compra
valor_final = valor - valor_desconto

#Exibe o resultado
print(f"\nValor da compra: R$ {valor:.2f}")
print(f"Desconto aplicado: {desconto*100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")
