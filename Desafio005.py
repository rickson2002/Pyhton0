# Este é um progorma de Python que recebe um caractere digitado pelo teclado utilizando a função input() e retorne, utilizando a função print(),
# esse caractere convertido em Decimal, Hexadecimal e Binário.

# Programa baisco em  Python 

letra = input("Digite um letra : ")
print("A letra que foi digitada é : {}" .format(letra))
print("O seu valor decimal é : ", ord(letra))
print("O seu valor binario é : ", bin(ord(letra)))
print("O seu valor hexadecimal é : ", hex(ord(letra)))