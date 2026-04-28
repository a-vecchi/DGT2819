# Array de Números
array = [17, 82, 2, 56, 5, 26, 90, 30, 76, 57, 42, 95, 80, 41, 35]

print("Números Desordenados:", array)

for i in range(len(array)):
    auxPos = i
    for j in range(i+1, len(array)):
        if array[auxPos] > array[j]:
            auxPos = j

    auxVal = array[i]
    array[i] = array[auxPos]
    array[auxPos] = auxVal

print("Números em Ordem Crescente:", array)