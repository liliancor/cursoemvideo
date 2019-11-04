t = input('Digite algo: ')
print('O tipo primitivo é {}'.format(type(t)))
print('É um número? {}'.format(t.isnumeric()))
print('É alfabético? {}'.format(t.isalpha()))
print('É alfanumérico? {}'.format(t.isalnum()))
print('Está em letras maiúsculas? {}'.format(t.isupper()))
print('Está em letras minúsculas? {}'.format(t.islower()))
print('Contem somente espaços? {}'.format(t.isspace()))
print('Está capitalizada?', t.istitle())

#t é um objeto. Todo objeto tem características e realiza funcionalidades, eles têm atributos e métodos. Como estes têm parênteses depois deles, eles têm métodos (isupper, etc...). 