def is_palindrome_recursive(arr, inicio=0, fim=None):

    if fim is None:
        fim = len(arr) - 1
        
    if inicio >= fim:
        return True
        
    if arr[inicio] != arr[fim]:
        return False

    return is_palindrome_recursive(arr, inicio + 1, fim - 1)


# ==========================================
# Testando os exemplos do slide
# ==========================================
if __name__ == "__main__":
    array1 = [0, 1, 2, 3, 2, 1, 0]
    array2 = ["a", "b", "b", "a"]
    array3 = ["a", "b", "c", "b", "a"]
    array4 = ["a", "b", "c", "f", "b", "a"]

    print("--- Resultados dos Testes ---")
    
    print(f"array1 -> {'É palíndromo' if is_palindrome_recursive(array1) else 'Não é palíndromo'}")
    print(f"array2 -> {'É palíndromo' if is_palindrome_recursive(array2) else 'Não é palíndromo'}")
    print(f"array3 -> {'É palíndromo' if is_palindrome_recursive(array3) else 'Não é palíndromo'}")
    print(f"array4 -> {'É palíndromo' if is_palindrome_recursive(array4) else 'Não é palíndromo'}")