def funcao(x):
    sequencia = [0, 1]

    while sequencia[-1] < x:
        proxima_sequencia = sequencia[-1] + sequencia[-2]
        sequencia.append(proxima_sequencia)

    if x in sequencia:
        return True
    else:
        return False

numero = int(input('Digite um numero:'))
if funcao(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")