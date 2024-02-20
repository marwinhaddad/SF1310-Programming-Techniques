
def spelplan(rader, kolumner):                  #   funktion för att kalla på spelplan
    lista = []                                  #   antalet rader och kolumner bestäms av användaren i main
    for rad in range(1, rader+1):
        radlista = []                           #   töm radlista för att stoppa in nästa rad
        for kolumn in range(1, kolumner+1):
            nr = str(rad) + str(kolumn)
            radlista.append(nr)                 #   "nästlad for-loop"
        lista.append(radlista)
        lista[0][0] = "P "
    return lista                                # return lista så att vi kan använda den i andra def


def skrivplan(plan):                            # funktion för att skriva ut spelplan
    for rad in plan:
        print(*rad)                             # "*" tar bort "[ ]"
    return plan

def chompa(plan, val):
    utlista = []                                # utlista är spelplanen efter modifieringen
    for lista in plan:
        radlista = []
        for nr in lista:        # .isalnum() förutsätter att input måste vara en sträng utan mellanrum
            if nr.isalnum():  # nr=talen på planen   #1                           #2
                if int(nr[0]) >= int(val[0]) and int(nr[1]) >= int(val[1]):
                    radlista.append("  ")
                else:
                    radlista.append(nr)
            else:
                radlista.append(nr)
        utlista.append(radlista)
    return utlista


def spelare(turer):             # funktion som bestämmer vems tur det är
    if turer % 2 == 0:
        return "Spelare 2"
    else:                       # returnerar spelarens tur
        return "Spelare 1"


def fel(val, lista):
    error = 0
    for rad in lista:           # kollar om vårt val finns i någon rad för varje rad i listan
        if val in rad:          # error = 1; vårt val finns. error = 0; vårt val finns INTE.
            error = 1
    nytt_val = val
    if error == 0:
        nytt_val = input("Välj något av de befintliga talen på planen: ")
        return fel(nytt_val, lista)
    return nytt_val


def vinst(lista, turer):
    if lista[0][1] == "  " and lista[1][0] == "  ":
        print("{} du vann!".format(spelare(turer)))
        return True


def main():
    turer = 0
    antal_rader = int(input("Välj antal rader: "))
    antal_kolumner = int(input("Välj antal kolumner: "))
    lista = spelplan(antal_rader, antal_kolumner)
    while True:
        if vinst(lista, turer):
            break
        turer += 1
        skrivplan(lista)
        val = input("{} välj: ".format(spelare(turer)))
        val = fel(val, lista)
        lista = chompa(lista, val)


main()
