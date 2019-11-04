n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('''A soma é {}; \nA multiplicação é {}; \nA divisão é {:.2f}; \nA divisão inteira é {}; \nA exponenciação é {}; \nO resto é {}.'''
.format(s, m, d, di, e, r))

#print('A soma é {} e a multiplicação é {}'.format(s, m), end='' como se eu falasse, end=a nada. Daí ele não quebra a linha na hora de imprimir a próxima linha. 
#print('.....