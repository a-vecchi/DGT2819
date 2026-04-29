import time

lista = list()

with open("documento.txt", "r", encoding="utf-8") as f:
    for linha in f:
        lista.extend(linha.split())

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
    return array

bubbleInicio = time.time()
listaBubble = bubbleSort(lista)
bubbleTempo = time.time()-bubbleInicio

def selectionSort(array):
    for i in range(len(array)):
        auxPos = i
        for j in range(i+1, len(array)):
            if array[auxPos] > array[j]:
                auxPos = j

        auxVal = array[i]
        array[i] = array[auxPos]
        array[auxPos] = auxVal
    return array

selectionInicio = time.time()
listaSelection = selectionSort(lista)
selectionTempo = time.time()-selectionInicio

def nativoSort(array):
    array.sort()
    return array

nativoInicio = time.time()
listaNativo = nativoSort(lista)
nativoTempo = time.time()-nativoInicio

print("Lista ordenadas - Bubble:")
print(listaBubble)
print(f"Tempo de Bubble: {bubbleTempo} segundos")

print("Lista ordenadas - Selection:")
print(listaSelection)
print(f"Tempo de Selection: {selectionTempo} segundos")

print("Lista ordenadas - Nativo:")
print(listaNativo)
print(f"Tempo de Nativo: {nativoTempo} segundos")

print(f"\nTempo de Bubble: {bubbleTempo} segundos")
print(f"Tempo de Selection: {selectionTempo} segundos")
print(f"Tempo de Nativo: {nativoTempo} segundos")

listaRapida = list()
if bubbleTempo < selectionTempo and bubbleTempo < nativoTempo:
    listaRapida = listaBubble
    print("Ordenação mais rápida Bubble")
elif selectionTempo < bubbleTempo and selectionTempo < nativoTempo:
    listaRapida = listaSelection
    print("Ordenação mais rápida Selection")
elif nativoTempo < bubbleTempo and nativoTempo < selectionTempo:
    listaRapida = listaNativo
    print("Ordenação mais rápida Nativo")

with open("documento_ordenado.txt", "w", encoding="utf-8") as f:
    for p in listaRapida:
        f.write(p + "\n")
