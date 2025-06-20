def subtrair(num1, num2):
    return (num1 - num2)


def somar(num1, num2):
    return (num1 + num2)

if __name__ == "__main__":
    # variaveis
    a = 5
    b = 8
    s = somar(a, b) # funcao para somar
    sub = subtrair(a, b) # funcao para subtrair
    print(f'Resultado da soma: {s}')
    print(f'Resultado da subtração eh: {sub}')
