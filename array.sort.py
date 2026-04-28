# Array de Números
arrayNumeros = [17, 82, 2, 56, 5, 26, 90, 30, 76, 57, 42, 95, 80, 41, 35]

print("Números Desordenados:", arrayNumeros)

arrayNumeros.sort()
print("Números em Ordem Crescente:", arrayNumeros)

arrayNumeros.sort(key=None, reverse=True)
print("Números em Ordem Decrescente:", arrayNumeros)

# Array de strings
arrayString = ["Alexandre", "1968-02-15", "207.555.080-84", "23.066.514-7"]

print("Strings Desordenadas:", arrayString)

arrayString.sort()
print("Strings em Ordem Crescente:", arrayString)

arrayString.sort(key=None, reverse=True)
print("Strings em Ordem Decrescente:", arrayString)