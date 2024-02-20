import random

tärningar = int(input("Hur många tärningar behövs i spelet? "))     #användaren matar in värdern för nödvändiga variabler
antal_kast = int(input("Hur många kast får vardera spelare? "))

def kast():                                    # skapar en funktion som vi kommer att kalla på senare
    tärningslista = []
    for x in range(tärningar):
        tärningslista.append(random.randint(1,6))  # för varje tal x i listan läggs det till ett slumpat tal mellan 1-6 i listan
        print("Tärning", str(x+1) + ": ",end="")
        print(tärningslista[x])                     # skriver ut talet i listan med index noll till och med -1
    print("Du fick: ", end="")
    for i, x in enumerate(tärningslista):         # återger värdena i listan
        if i == len(tärningslista)-1:
            print(x, end=".\n")
        else:
            print(x, end=", ")
    print()


while True:
    kast_count = antal_kast
    avsluta = input("Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A: ")
    if avsluta == "A":
        break
    kast()
    kast_count -= 1
    while kast_count > 0:           # så länge kas_count är större än  noll komemr den fråga om man vill kasta igen
        igen = input("Är du inte nöjd kan du kasta igen, vill du kasta igen?(j/n) ")
        if igen != "j":
            break
        kast()
        kast_count -= 1


