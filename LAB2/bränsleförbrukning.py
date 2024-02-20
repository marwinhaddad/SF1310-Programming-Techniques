km = float(input("Ange körsträcka i km:"))
liter =float(input("Ange förbrukat bräsnle i liter:"))
bf = round((liter/km)*100, 3)
print("bräsnleförbrukningen för bilen är", bf,"l/100km")