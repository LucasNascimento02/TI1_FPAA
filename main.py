def karatsuba(numero1, numero2):
    if numero1 < 10 or numero2 < 10:
        return numero1 * numero2
    
    num_digitos = max(len(str(numero1)), len(str(numero2)))
    meio = num_digitos // 2
    
    divisor = 10 ** meio
    
    parte_alta1 = numero1 // divisor
    parte_baixa1 = numero1 % divisor
    parte_alta2 = numero2 // divisor
    parte_baixa2 = numero2 % divisor
    
    produto_altas = karatsuba(parte_alta1, parte_alta2)  # ac
    produto_baixas = karatsuba(parte_baixa1, parte_baixa2)  # bd
    produto_soma = karatsuba(parte_alta1 + parte_baixa1, 
                           parte_alta2 + parte_baixa2)  # (a+b)(c+d)
    
    # (ad + bc) = (a+b)(c+d) - ac - bd
    termo_meio = produto_soma - produto_altas - produto_baixas
    
    # ac * 10^(2m) + (ad + bc) * 10^m + bd
    return (produto_altas * 10**(2*meio) + 
            termo_meio * 10**meio + 
            produto_baixas)

def test_karatsuba(x, y):
    """Função auxiliar para testar o algoritmo de Karatsuba."""
    resultado_karatsuba = karatsuba(x, y)
    resultado_python = x * y
    print(f"\nTestando: {x} × {y}")
    print(f"{'=' * 50}")
    print(f"Resultado Karatsuba: {resultado_karatsuba}")
    print(f"Resultado Python:    {resultado_python}")
    print(f"Correto: {'✓' if resultado_karatsuba == resultado_python else '✗'}")
    return resultado_karatsuba == resultado_python

def main():
    print("DEMONSTRAÇÃO DO ALGORITMO DE KARATSUBA")
    print("=" * 40)
    
    casos_teste = [
        (4, 5),
        (12, 13),
        
        (1234, 5678),
        (9999, 9999),
        
        (12345678, 87654321),
        (123456789, 987654321),
        
        (1000, 1000),
        (10000, 10000),
        
        (1002003, 3002001),
        (1000000, 1000001)
    ]
    
    total_testes = len(casos_teste)
    testes_corretos = 0
    
    for x, y in casos_teste:
        if test_karatsuba(x, y):
            testes_corretos += 1
    
    print("\nRELATÓRIO FINAL")
    print("=" * 40)
    print(f"Total de testes: {total_testes}")
    print(f"Testes corretos: {testes_corretos}")
    print(f"Precisão: {(testes_corretos/total_testes)*100:.2f}%")

if __name__ == "__main__":
    main() 