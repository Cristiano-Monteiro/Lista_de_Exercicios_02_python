ladoA = int(input('Lado A do triângulo: '))
ladoB = int(input('Lado B do triângulo: '))
ladoC = int(input('Lado C do triângulo: '))
forma_triangulo = (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA)
equilatero = ladoA == ladoB == ladoC
isosceles = (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC)
escaleno = ladoA != ladoB != ladoC
if(forma_triangulo):
    if(equilatero):
        print('Os 3 lados FORMAM um triângulo Equilátero!')
    elif(isosceles):
        print('Os 3 lados FORMAM um triângulo Isósceles!')
    else:
        print('Os 3 lados FORMAM um triângulo Escaleno!')
else:
    print('Os 3 lados NÃO formam um triângulo!')