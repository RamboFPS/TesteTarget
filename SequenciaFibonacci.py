def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return n == b

def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    if sequence[-1] == n:
        print(f"{n} pertence à sequência de Fibonacci")
    else:
        print(f"{n} não pertence à sequência de Fibonacci")

numero = int(input("Digite um número: "))
fibonacci_sequence(numero)
