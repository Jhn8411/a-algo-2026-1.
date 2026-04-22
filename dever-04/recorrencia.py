import math

def f_recursivo(n):

    if n == 1:
        return 2
    
    return 2 * f_recursivo(n - 1) + (n ** 2)


def f_formula_fechada(n):

    termo_exponencial = 13 * math.pow(2, n - 1)
    
    return int(termo_exponencial - (n ** 2) - 4 * n - 6)


def executar_tarefa():
    print("--- Calculadora de Relação de Recorrência ---")
    
    entrada = input("Digite um valor inteiro para n (ex: 5): ")
    
    try:
        n = int(entrada)
        
        if n < 1:
            print("O caso base é F(1). Por favor, insira um valor de n >= 1.")
            return
            
        resultado_rec = f_recursivo(n)
        print(f"\nResultado usando Recursão F({n}): {resultado_rec}")
        
        resultado_fec = f_formula_fechada(n)
        print(f"Resultado usando Fórmula Fechada F({n}): {resultado_fec}")
        
    except ValueError:
        print("Entrada inválida. Por favor, certifique-se de digitar um número inteiro.")
        
    except RecursionError:
        print(f"\nErro: O valor de n={n} é muito grande e excedeu o limite de recursão do Python!")
        print(f"Mas a fórmula fechada consegue calcular: {f_formula_fechada(n)}")

if __name__ == "__main__":
    executar_tarefa()