n = int(input("Quantos números da sequência de Fibonacci você deseja gerar? "))

fibonacci_anterior = 0
fibonacci_atual = 1


if n <= 0:
    print("Por favor, forneça um número positivo.")
elif n == 1:
    print("Sequência de Fibonacci até o número", n, ":")
    print(fibonacci_anterior)
else:
    print("Sequência de Fibonacci até o número", n, ":")
    print(fibonacci_anterior)
    print(fibonacci_atual)
    for i in range(2, n):
        fibonacci_proximo = fibonacci_anterior + fibonacci_atual
        print(fibonacci_proximo)
        fibonacci_anterior = fibonacci_atual
        fibonacci_atual = fibonacci_proximo
        