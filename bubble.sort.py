def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux

# Array de Números
arrayNumeros = [17, 82, 2, 56, 5, 26, 90, 30, 76, 57, 42, 95, 80, 41, 35]

print("Números Desordenados:", arrayNumeros)

bubbleSort(arrayNumeros)

print("Números em Ordem Crescente:", arrayNumeros)