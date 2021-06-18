#SumTwoNumbers: That receives two numbers and returns the sum of both


'''Dentro de bloque protegido para poder capturar la excepcion ValueError en caso de no ingresar numeros '''

try:
    num1 = int(input("Por favor ingrese un número: "))
    num2 = int(input("Por favor ingrese otro número: "))
    sum = num1 + num2
    print("La suma de ambos numeros es:" ,sum)
    
except ValueError:
    print("Por favor, sólo ingrese numeros")
