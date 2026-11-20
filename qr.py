print('calculadora de área')
print('selecione a figura geometrica \n1-triangulo \n2-trapézio \n3-quadrado \n4-circulo')
escolha = int(input('digite o numero da figura: '))
try:
    if escolha ==1:
        base = float(input('digite a base do triangulo: '))
        altura = float(input('digite a altura do triangulo: '))
        area = (base * altura) / 2
        print(f'a area do triangulo é {area}')
    elif escolha ==2:
        base_maior = float(input('digite a base maior do trapézio: '))
        base_menor = float(input('digite a base menor do trapézio: '))
        altura = float(input('digite a altura do trapézio: '))
        area = ((base_maior + base_menor) * altura) / 2
        print(f'a area do trapézio é {area}')
    elif escolha ==3:
        lado = float(input('digite o lado do quadrado: '))
        area = lado ** 2
        print(f'a area do quadrado é {area}')
    elif escolha ==4:
        raio = float(input('digite o raio do circulo: '))
        area = 3.14 * (raio ** 2)
        print(f'a area do circulo é {area}')
except ValueError: 
    print('por favor, digite um numero valido') 