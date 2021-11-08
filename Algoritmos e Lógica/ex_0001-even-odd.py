# Task
# Given an integer, n, perform the followind conditional actions:
#  - if n is odd, print Weird
#  - if n is even and in the incluse range of 2 to 5, print Not Weird
#  - if n is even and in the inclusive range of 6 to 20, print Weird
#  - if n is even and greater than 20, print Not Weird
# Constraints
#  - 1 <= n <= 100

class ValorForaIntervalo(Exception):
    pass


while True:
    try:
        n = int(input('Digite um número entre 1 e 100: '))
        if n not in range(1, 101):
            raise ValorForaIntervalo
        if n % 2 == 0 and n > 20 or n % 2 == 0 and 2 >= n <= 5:
            print('Not Weird')
        else:
            print('Weird')
        break
    except ValueError:
        print('Digite um valor numérico válido entre 1 e 100!')
    except ValorForaIntervalo:
        print("Escolha um número entre 1-100")
