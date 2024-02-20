rader = int(input("Ange antal rader: "))
kolumner = int(input("Ange antal kolumner: "))

rad_count = 1
kol_count = 1

print("    ", end="")
for x in range(kolumner):
    print("{0:<4d}".format(x + 1), end="")
print("")

while rad_count-1 < rader:
    print(rad_count, end="   ")
    kol_count = 1
    while kol_count-1 < kolumner:

        print("{0:<4d}".format(kol_count * rad_count), end="")
        kol_count += 1
    print("")
    rad_count += 1
