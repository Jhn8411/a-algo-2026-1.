import time
import sys

sys.setrecursionlimit(2000)

def factorial_recursivo(n):

    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial_recursivo(n - 1)

def executar_experimento():
    valores_n = [10, 100, 500, 1000]
    
    print("--- Medição de Tempo: Factorial Recursivo ---\n")
    
    for n in valores_n:
        inicio = time.time()
        
        _ = factorial_recursivo(n)
        
        fim = time.time()
        
        tempo_execucao = fim - inicio

        print(f"n = {n:<4} | Tempo de execução: {tempo_execucao:.6f} segundos")

if __name__ == "__main__":
    executar_experimento()

"""
=========================================================
ANÁLISE DE COMPLEXIDADE ASSINTÓTICA
=========================================================

Complexidade de Tempo: O(n) (Linear)
- Raciocínio: Quando chamamos a função para 'n', ela invoca
  a si mesma 'n' vezes até atingir o caso base (n=1 ou n=0).
  Como cada execução individual realiza operações de tempo
  constante O(1) (comparação, subtração e multiplicação), 
  o tempo total cresce proporcionalmente a 'n'.

Complexidade de Espaço: O(n)
- Raciocínio: Sendo um algoritmo recursivo, cada chamada
  fica armazenada na memória (call stack) aguardando as 
  próximas finalizarem. Para n=1000, temos 1000 chamadas
  empilhadas, o que torna o uso de memória linear.
=========================================================
"""