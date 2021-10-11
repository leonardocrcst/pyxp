hpValue = int(input("Saúde base: "))
axieLevel = int(input("Nível do Axie: "))

maxHP = int((hpValue * 6 + 150) * 1.05 ** (axieLevel - 1))

print("Saúde máxima do Axie: {mhp}".format(mhp=maxHP))