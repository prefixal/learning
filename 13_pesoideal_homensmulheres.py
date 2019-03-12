altura = float(input("Digite sua altura: "))
genero = int((input("Se homem digite 0, se mulher digite 1: ")))

if genero == 0:
    ideal = (72.7*altura) - 58
    
    printa = "homens"

else:
    ideal = (62.1*altura) - 44.7
    printa = "mulheres"

print("Você tem {:.2f}m de altura, o peso ideal para {} de sua altura é de {:.2f}kg".format(altura, printa,ideal))



