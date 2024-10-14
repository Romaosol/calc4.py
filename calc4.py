python
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("0. Sair")

while True:
    menu()
    choice = input("Digite a sua escolha: ")

    if choice == '0':
        break

    num1 = float(input("Digite o primeiro número: "))

    if choice == '6':
        print("Resultado:", sqrt(num1))
    else:
        num2 = float(input("Digite o segundo número: "))

        if choice == '1':
            print("Resultado:", add(num1, num2))
        elif choice == '2':
            print("Resultado:", subtract(num1, num2))
        elif choice == '3':
            print("Resultado:", multiply(num1, num2))
        elif choice == '4':
            print("Resultado:", divide(num1, num2))
        elif choice == '5':
            print("Resultado:", power(num1, num2))
        else:
            print("Opção inválida!")

print("Calculadora encerrada.")
