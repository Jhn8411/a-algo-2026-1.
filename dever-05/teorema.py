import math

def calcular_teorema_mestre(a, b, c, descricao_f):

    log_b_a = math.log(a, b)
    
    print(f"Analisando: T(n) = {a}T(n/{b}) + {descricao_f}")
    print(f"- Parâmetros extraídos: a = {a}, b = {b}, grau de f(n) = {c}")
    print(f"- Calculando critério: log_{b}({a}) = {log_b_a}")

    if math.isclose(c, log_b_a):
        print("- Conclusão: c == log_b(a) -> Encaixa no CASO 2 do Teorema Mestre.")

        expoente = int(c) if c.is_integer() else c
        if expoente == 0.5:
            print("- Resultado Final: Theta(sqrt(n) * log n)\n")
        elif expoente == 1:
            print("- Resultado Final: Theta(n * log n)\n")
        else:
            print(f"- Resultado Final: Theta(n^{expoente} * log n)\n")
            
    elif c > log_b_a:
        print("- Conclusão: c > log_b(a) -> Encaixa no CASO 3 do Teorema Mestre.")
        expoente = int(c) if c.is_integer() else c
        
        if expoente == 1:
            print("- Resultado Final: Theta(n)\n")
        else:
            print(f"- Resultado Final: Theta(n^{expoente})\n")
            
    else:
        print("- Conclusão: c < log_b(a) -> Encaixa no CASO 1 do Teorema Mestre.")
        expoente = int(log_b_a) if log_b_a.is_integer() else log_b_a
        print(f"- Resultado Final: Theta(n^{expoente})\n")


def gerar_relatorio_aula5():

    print("==================================================")
    print("   ANALISADOR DE COMPLEXIDADE - DEVER DE CASA 5   ")
    print("==================================================\n")
    
    print("1) Algoritmo de Ordenação Merge Sort")
    print("--------------------------------------------------")
    print("A cada passo, o Merge Sort divide o array em 2 (T(n/2)).")
    print("O processo de fusão (merge) custa tempo linear (O(n)).")
    print("Isso gera a recorrência T(n) = 2T(n/2) + n.")
    calcular_teorema_mestre(2, 2, 1.0, "n")
    
    print("2) Multiplicação de Matrizes (Algoritmo Clássico)")
    print("--------------------------------------------------")
    print("Para multiplicar matrizes quadradas nxn, o algoritmo padrão")
    print("utiliza 3 laços 'for' aninhados (iterando sobre linhas,")
    print("colunas e somando o produto escalar).")
    print("Cálculo: O(n) * O(n) * O(n) = O(n^3)")
    print("- Resultado Final: O(n^3)\n")
    
    print("3) Resolução de Recorrências")
    print("--------------------------------------------------")
    
    # Letra A: T(n) = 2T(n/4) + raiz(n) 
    # O grau de f(n) é 0.5 (pois raiz de n é n elevado a 1/2)
    calcular_teorema_mestre(2, 4, 0.5, "sqrt(n)")
    
    # Letra B: T(n) = 2T(n/4) + n
    # O grau de f(n) é 1 (pois n é n elevado a 1)
    calcular_teorema_mestre(2, 4, 1.0, "n")
    
    # Letra C: T(n) = 16T(n/4) + n^2
    # O grau de f(n) é 2 (pois n está elevado ao quadrado)
    calcular_teorema_mestre(16, 4, 2.0, "n^2")

if __name__ == "__main__":
    gerar_relatorio_aula5()