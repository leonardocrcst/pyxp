print("Calculadora de juros")
print("--------------------")
inicial = float(input("Valor inicial: "))
juromes = float(input("Taxa de juros mensal: ")) / 100
periodo = int(input("Período (meses): "))
print("--------------------")
final = inicial * (1 + juromes) ** periodo
difer = final - inicial
print("Em {periodo} meses você terá {final:.2f}, uma diferença de {difer:.2f}".format(periodo=periodo, final=final, difer=difer))