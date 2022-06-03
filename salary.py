htworked = int(input('Inform the number of hours worked: '))
hextra = int(input('Enter the number of overtime hours: '))
vhour = int(input('Write the value of the hour: '))
hovertime = int
sbruto = int
inss = int
fgts = int
sliquid = int

hovertime = 100

sbruto = htworked + hextra * (1 + (hovertime / 100)) * vhour
inss = sbruto * 9/100
fgts = sbruto * 8/100
sliquid = sbruto - inss

print('The gross salary is:', sbruto)
print('The net salary is: ', sliquid)
print('The INSS is', inss)
print('The FGTS is', fgts)
