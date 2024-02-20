from tvkontroll import Tv


def huvudmeny():
    print("*** Välkommen till TV-Simulatorn ***\n")
    with open("tvtext.txt", "r", encoding="utf-8") as f:
        meny1 = f.readlines()
        raknare = 1
        for rad in meny1:
            radsplit = rad.split(" ")
            print(str(raknare) + ". " + (radsplit[0]))
            raknare += 1
    print(str(raknare) + ".", "Avsluta\n")


def error(input_, minst, storst):
    while True:
        try:
            input_ = int(input_)
            if minst <= int(input_) <= storst:
                return input_
            input_ = input("Vänligen ange ett tal mellan {} och {}: ".format(minst, storst))
        except ValueError:
            input_ = input("Vänligen ange ett tal som finns ovan: ")


def valtv():
    with open("tvtext.txt", "r", encoding="utf-8") as f:
        lista = []
        for rader in f:
            lista.append(rader.strip("\n").split(", "))
    return lista


def skrivafil(lista):
    with open("tvtext.txt", "w", encoding="utf-8") as f:
        for rad, tv in enumerate(lista):
            string = ", ".join(map(str, tv))
            for grej in string:
                f.write(grej)
            f.write("\n")


def menytv():
    print("\n1. Byt kanal\n2. Höj ljudvolym\n3. Sänk volym\n4. Återgå till huvudmenyn\n")


def main():
    while True:

        antalrader = len(open("tvtext.txt", "r").readlines())
        huvudmeny()
        input_1 = input("Välj TV: ")
        input_1 = error(input_1, 1, antalrader + 1) - 1
        if input_1 + 1 == int(antalrader+1):
            print("Simulationen avslutad.")
            break
        tvradlista = valtv()

        while True:
            obj = Tv(tvradlista[input_1][0], int(tvradlista[input_1][1]), int(tvradlista[input_1][2]),
                     int(tvradlista[input_1][3]), int(tvradlista[input_1][4]))
            print(obj.tvmeny())
            menytv()
            input_2 = input("Välj funktion: ")
            input_2 = error(input_2, 1, 4)

            if input_2 == 1:
                kanalnr = input("Ange kanalnummer: ")
                kanalnr = error(kanalnr, 1, int(tvradlista[input_1][1]))
                tvradlista[input_1][2] = kanalnr

            elif input_2 == 2:
                tvradlista[input_1][4] = obj.ljudupp()

            elif input_2 == 3:
                tvradlista[input_1][4] = obj.ljudner()

            elif input_2 == 4:
                break
            skrivafil(tvradlista)


main()
