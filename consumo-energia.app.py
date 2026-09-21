nome = input("Digite o nome do aparelho: ")

potencia = float(input("Digite a potência do aparelho em watts (W): "))

horasDia = float(input("Digite o tempo médio de uso diário em horas: "))

consumoMensal = (potencia * horasDia * 30) / 1000

custo = consumoMensal * 0.75

print("\n--- Resultado ---")
print(f"Aparelho: {nome}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f}")