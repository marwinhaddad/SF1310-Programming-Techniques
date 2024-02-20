antal_paket = int(input("Hur många paket vill du skicka?"))
lista_paket = []
i = 0

while i < antal_paket:
    print("Ange vikt för paket", end=" ")
    print(i+1, end=":")
    kg = float(input())
    i += 1
    if kg < 2:
        lista_paket.append(kg*30)
    elif 2 <= kg < 6:
        lista_paket.append(kg*28)
    elif 6 <= kg < 12:
        lista_paket.append(kg*25)
    elif 12 <= kg:
        lista_paket.append(kg*23)

print("Det kommer att kosta", sum(lista_paket),"Kr")