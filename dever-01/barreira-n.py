import time
import random

TAMANHOS_TESTE = [1000, 5000, 10000, 20000, 50000]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

def executar_experimento():
    
    print("Iniciando a comparação empírica de algoritmos...\n")
    
    for n in TAMANHOS_TESTE:
        print(f"--- Testando para n = {n} ---")
        
        lista_original = [random.randint(0, 100000) for _ in range(n)]
        
        lista_insertion = lista_original.copy()
        lista_timsort = lista_original.copy()
        
        inicio_insertion = time.time()
        insertion_sort(lista_insertion)
        fim_insertion = time.time()
        tempo_insertion = fim_insertion - inicio_insertion
        
        inicio_timsort = time.time()
        sorted(lista_timsort)
        fim_timsort = time.time()
        tempo_timsort = fim_timsort - inicio_timsort
        
        print(f"Tempo Insertion Sort O(n^2) : {tempo_insertion:.6f} segundos")
        print(f"Tempo Timsort O(n log n)    : {tempo_timsort:.6f} segundos")
        
        if tempo_timsort > 0:
            print(f"O Timsort foi {tempo_insertion / tempo_timsort:.2f}x mais rápido.\n")
        else:
            print("O Timsort foi rápido demais para ser medido.\n")

if __name__ == "__main__":
    executar_experimento()