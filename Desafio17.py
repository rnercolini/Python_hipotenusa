# Calcula a hipotenusa de um triângulo retângulo
from math import hypot
cat1 = float(input('Digite o tamanho do cateto oposto: '))
cat2 = float(input('Digite o tamanho do cateto adjacente: '))
hip = hypot(cat1, cat2)
print('Para os catetos {0} e {1}, a hipotenusa é {2:.2f}'.format(cat1, cat2, hip))
