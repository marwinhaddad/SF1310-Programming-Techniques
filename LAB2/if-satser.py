kg = float(input("Hur mycket väger paketet:"))
if kg < 2:
    print("Det kommer att kosta", kg * 30, "Kr")
elif 2 <= kg < 6:
    print("Det kommer att kosta", kg * 28, "Kr")
elif 6 <= kg < 12:
    print("Det kommer att kosta", kg * 25, "Kr")
elif 12 < kg:
    print("Det kommer att kosta", kg * 23, "Kr")