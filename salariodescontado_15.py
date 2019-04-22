pmt = float(input('Quanto você ganha por hora?'))
hour = int(input('Número de horas trabalhadas no mês: '))

bruto = pmt * hour
inss = 0.08*bruto
sind = 0.05*bruto
ir = 0.11*bruto

print('(+) Salário Bruto   : R$ {:.2f}'.format(bruto))
print('(-) IR (11%)        : R$ {:.2f}'.format(ir))
print('(-) INSS (8%)       : R$ {:.2f}'.format(inss))
print('(-) Sindicato (5%)  : R$ {:.2f}'.format(sind))
print('(=) Salário Líquido : R$ {:.2f}'.format(bruto - (inss + sind + ir)))



