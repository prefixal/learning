#limite 50 quilos;
# multa 4 pila por excedente

peso = float(input("Quantos quilos de peixe pescado? (kg): "))

excesso = peso - 50

if excesso > 0:
    multa = excesso*4
    tem = "há multa"
    print("Multa no valor de R${:.2f}".format(multa))


print("Você pescou {:.2f}kg de peixe".format(peso))

