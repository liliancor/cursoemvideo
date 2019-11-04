nota1 = float(input('nota_primeiro_bimestre: ')) #.replace(',', '.'))#
nota2 = float(input('nota_segundo_bimestre: '))
m = (nota1 + nota2)/2
print('As notas foram {:.1f} e {:.1f} e a média é {:.1f}'.format(nota1, nota2, m))