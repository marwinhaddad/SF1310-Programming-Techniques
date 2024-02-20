# Namn: Marwin Haddad
# Program: COPEN
# Uppgift 137 Solkraftverk
# Datum: 2021-08-27

import tkinter
from tkinter import *
from tkinter import messagebox, scrolledtext
import matplotlib
import pandas as pd
import random
import math
import statistics as st
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('tkagg')


# Kraftverks klass, __init__ definierar attribut som sol- och vindkraftverk har gemensamt

class Kraftverk:
    def __init__(self):
        self.entry = None
        self.lista = []
        self.lista_effekt = []
        self.lista_effekt_månad = []
        self.månader = ['Jan', 'Feb', 'Mar', 'Apr', 'Maj', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']

    # Skapar en sträng av all data för att kunna klistra fast det i Toplevel-fönster

    def skapa_sträng(self):
        self.sträng = self.rubrik
        for _ in self.sträng:
            self.sträng += "="
        for i in range(12):  # månad: wt max, min, medel och stdav. för varje mån
            self.sträng += ('\n\n{}:\nMax: {} Min: {} Med: {} Stdav: {}\n'.format(self.månader[i],
                                                                                  str(self.data['Max'][i]),
                                                                                  str(self.data['Min'][i]),
                                                                                  str(self.data['Medel'][i]),
                                                                                  str(self.data['Stdav'][i])))
            self.sträng += pd.DataFrame(self.lista[30 * i:30 + 30 * i]).to_string(index=False, header=False)

        self.sträng += ('\n\nMedelvärde: {} Standardavvikelse: {}'.format(str(round(st.mean(self.data['Medel']), 2)),
                                                                          str(round(st.stdev(self.data['Stdav']), 2))))

    # Skapar en dict med listor av värden som änvänds i metoderna "Skapa_sträng", "diagram" och "tabell"

    def ny_data(self):
        self.data = {'Max': np.round(list(map(max, self.lista_effekt_månad)), 2),
                     'Min': np.round(list(map(min, self.lista_effekt_månad)), 2),
                     'Medel': np.round(list(map(st.mean, self.lista_effekt_månad)), 2),
                     'Stdav': np.round(list(map(st.stdev, self.lista_effekt_månad)), 2),
                     'Total': np.round(list(map(sum, self.lista_effekt_månad)), 2)}

    # Kallar på funktionerna som skapar alla attr som definierar objektet, tex. listor, och dict med data

    def ny_attr(self):
        self.lista_effekt_månad = []
        self.lista = []
        self.lista_effekt = []
        self.nya_listor()
        self.ny_data()
        self.skapa_sträng()

    # Öppnar ett diagram i matplotlib med genererad data på medelvärde per månad

    def diagram(self):
        if error_knapptryckning(self.entry):
            plt.figure('Diagram - ' + self.val[1] + str(self.entry))
            plt.bar(self.månader, self.data['Medel'])
            plt.title(self.val[0].capitalize() + self.val[1] + str(self.entry) +
                      '\nGenomsnittlig energiproduktion per månad för ' + self.val[0].capitalize())
            plt.xlabel('Månad')
            plt.ylabel('Kilowatt')
            plt.show()
        else:
            pass

    # Öppnar en tabell i matplotlib med genererad data

    def tabell(self):
        if error_knapptryckning(self.entry):
            dataf = pd.DataFrame(self.data, index=self.månader).round(decimals=2)
            plt.figure('Tabell - ' + self.val[0] + str(self.entry))
            plt.title(self.val[0].capitalize() + self.val[1] + str(self.entry) + '\nTabellvärden')
            plt.table(cellText=dataf.values, rowLabels=self.månader, cellLoc='center', loc='center',
                      colLabels=dataf.columns)
            plt.axis(False)
            plt.show()
        else:
            pass


# Underklass till Kraftverk. Definierar Solkraftverk. Solkraftverk kommer hämta attribut från moderklassen Kraftverk
# samtidigt som den definierar egna attribut som är speciella för ett solkraftverk.

class Solkraftverk(Kraftverk):
    def __init__(self):
        super().__init__()
        self.val = ('solkraftverk', 'latitud: ')
        self.area = 450
        self.soltal = 3000 / self.area
        self.rubrik = "Solkraftverk\n\nArea | Soltal | Latitud | Dag | Solighetsfaktor | f(t, latitud) | W(t)\n"

    # Effektfunktion som returnerar effekten. Inparametrar är energin "j" och ett slumpmässigt tal mellan 0 och 1

    def effekt(self, j, solighetsfaktor):
        return round(self.area * solighetsfaktor * self.soltal * j, 2)

    # Energifunktion som returnerar allstrad energi per dag. Inparameter dag.

    def energi(self, dag):
        j = (23.5 * math.sin((math.pi * (dag - 80)) / 180) + 90 - int(self.latitud)) / 90
        if 0 < j < 1:
            j = j ** 2
        elif j <= 0:
            j = 0
        elif j >= 1:
            j = 1
        return j

    # Genererar lista med nödvändiga värden för att skapa texten samt listan med effekt per månad per dag med hjälp av
    # metoden effekt_per_månad tillhörande moderklassen Kraftverk

    def nya_listor(self):
        self.latitud = self.entry

        for dag in range(1, 361):
            solighetsfaktor = random.random()
            j = self.energi(dag)
            w = self.effekt(j, solighetsfaktor)
            self.lista.append([self.area, round(self.soltal), self.latitud, dag,
                               round(solighetsfaktor, 1), round(j, 2), round(w, 2)])
            self.lista_effekt.append(w)
        for i in range(12):
            self.lista_effekt_månad.append(self.lista_effekt[30*i:30+30*i])


# Underklass till Kraftverk. Definierar Vindkraftverk. Vindkraftverk kommer hämta attribut från moderklassen Kraftverk
# samtidigt som den definierar egna attribut som är speciella för ett vindkraftverk.

class Vindkraftverk(Kraftverk):
    def __init__(self):
        super().__init__()
        self.rotorarea = None
        self.val = ('vindkraftverk', 'rotordiameter: ')
        self.luftdensitet = 1.225
        self.rubrik = "Vindkraftverk\n\nRotorarea | Luftdensitet | Rotordiameter | Dag | Vindhastighet(m/s) | W(t)\n"

    # Beräknar rotorarean med hälp av rotordiametern (entry)

    def area(self):
        self.rotorarea = math.pi * math.pow((int(self.rotordiameter) / 2), 2)

    # Effektfunktion som returnerar effekten. Inparameter är vindhastigheten "v"

    def effekt(self, v):
        return (self.rotorarea * self.luftdensitet * v ** 3) / 2

    # Funktion som bestämmer vindhastigheten per dag. Vindhastigheten varierar beroende på årstid. Ges i m/s

    def vindhastighet(self, dag):
        if dag <= 60 or 150 < dag <= 240 or 330 < dag:
            v = round(random.uniform(1, 9), 1)
        else:
            v = round(random.uniform(2, 11), 1)
        return v

    # Genererar lista med nödvändiga värden för att skapa texten samt listan med effekt per månad per dag med hjälp av
    # metoden effekt_per_månad tillhörande moderklassen Kraftverk

    def nya_listor(self):
        self.rotordiameter = self.entry
        self.area()
        for dag in range(1, 361):
            v = self.vindhastighet(dag)
            w = self.effekt(v)
            self.lista.append([round(self.rotorarea), self.luftdensitet, self.rotordiameter, dag, round(v, 2), round(w, 2)])
            self.lista_effekt.append(w)
        for i in range(12):
            self.lista_effekt_månad.append(self.lista_effekt[30*i:30+30*i])


# Interface-klass. Inparametrar är solkraftverks- och vindkraftverksobjektet.

class Gui:
    def __init__(self, Solkraftverk, Vindkraftverk):
        self.solkraftverk = Solkraftverk
        self.vindkraftverk = Vindkraftverk
        self.master = Tk()
        self.master.title('Kraftverk-SIM')

        self.textsol = Label(self.master, text='Solkraftverk: \nAnge latitud mellan 1 - 89.')
        self.textsol.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.entrysol = Entry(self.master, width=50, borderwidth=5)
        self.entrysol.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.knappSD = Button(self.master, text='Solkraftverk: \nDiagram',
                              command=lambda: self.solkraftverk.diagram())
        self.knappST = Button(self.master, text='Solkraftverk:\nTabell',
                              command=lambda: self.solkraftverk.tabell())
        self.knappStxt = Button(self.master, text='Solkraftverk:\nTextfil',
                                command=lambda: self.öppna_text(self.solkraftverk))
        self.knappSny = Button(self.master, text='Solkraftverk:\nGenerera nya värden',
                               command=lambda: self.hämta(self.solkraftverk, self.entrysol, 1, 89, 2, 4))

        self.knappSD.grid(row=2, column=0, padx=35, pady=20)
        self.knappST.grid(row=2, column=1, padx=35, pady=20)
        self.knappStxt.grid(row=2, column=2, padx=35, pady=20)
        self.knappSny.grid(row=1, column=4, padx=35, pady=20)

        self.textvind = Label(self.master, text='\nVindkraftverk: \nAnge rotordiameter mellan 26 - 49.')
        self.textvind.grid(row=3, columnspan=4, padx=10, pady=10)
        self.entryvind = Entry(self.master, width=50, borderwidth=5)
        self.entryvind.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

        self.knappVD = Button(self.master, text='Vindkraftverk:\nDiagram',
                              command=lambda: self.vindkraftverk.diagram())
        self.knappVT = Button(self.master, text='Vindkraftverk:\nTabell',
                              command=lambda: self.vindkraftverk.tabell())
        self.knappVtxt = Button(self.master, text='Vindkraftverk:\nTextfil',
                                command=lambda: self.öppna_text(self.vindkraftverk))
        self.knappVny = Button(self.master, text='Vindkraftverk:\nGenerera nya värden',
                               command=lambda: self.hämta(self.vindkraftverk, self.entryvind, 26, 49, 5, 4))

        self.knappVD.grid(row=5, column=0, padx=37, pady=20)
        self.knappVT.grid(row=5, column=1, padx=41, pady=20)
        self.knappVtxt.grid(row=5, column=2, padx=41, pady=20)
        self.knappVny.grid(row=4, column=4)

        self.knappAV = Button(self.master, text='Avsluta programmet', command=lambda: self.avsluta())
        self.knappAV.grid(row=6, column=1, padx=41, pady=20)
        self.master = mainloop()

    # Uppdaterar nuvarande sparat värde på sidan. Inparameter vilken typ av kraftverk(str), användarinput, rad och kolumn
    # som kommer att uppdateras på sidan och entrywidgeten som ska tömmas

    def nuvarande(self, typ, entry, rad, kol, entrywidget):
        värde = Label(self.master, text='Nuvarande ' + typ + '\n' + entry)
        värde.grid(row=rad, column=kol)
        entrywidget.delete(0, END)

    # Hämtar givet värde i GUI:ns entrywidgets för att kunna uppdatera kraftverkens latitud/ rotordiameter för Solkraftverk
    # resp. Vindkraftverk. Inparametrar är objektet, entrywidget, minsta tillåtna värde, största tillåtna värde samt vilken
    # rad och kolumn som ska uppdateras på sidan

    def hämta(self, obj, entry, minsta, största, rad, kol):
        if error_inmatning(entry.get(), minsta, största):
            obj.entry = entry.get()
            obj.ny_attr()
            self.nuvarande(obj.val[1], entry.get(), rad, kol, entry)
        else:
            pass

    # Öppnar ett nytt fönster och klistrar in strängen som genereras i Kraftverk.skapa_sträng(). Inparameteran är objektet
    # vars sträng man vill öppna.

    def öppna_text(self, obj):
        if error_knapptryckning(obj.entry):
            top = Toplevel(self.master)
            area = scrolledtext.ScrolledText(top, width=100, height=40)
            area.insert(tkinter.INSERT, obj.sträng)
            area.configure(state="disabled")
            area.pack()
            spara = Button(top, text='Spara textfil',
                           command=lambda: sparaText(obj.val[0], obj.entry, obj.sträng))
            spara.pack(padx=35, pady=15)
            top.mainloop()
        else:
            pass

    # Stänger alla öppna fönster och avslutar programmet

    def avsluta(self):
        self.master.destroy()
        plt.close('all')
        exit()


# Errorfunktion. Testar ifall inmatning är en int och ifall det värdet ligger mellan största och minsta.
# Ifall input inte stämmer öppnas ett error-meddelande med felkod.

def error_inmatning(entry, minst, störst):
    try:
        int(entry)
        if minst <= int(entry) <= störst:
            return True
        else:
            messagebox.showerror('Value Error',
                                 'Vänligen ange ett heltal mellan {} och {}.'.format(str(minst), str(störst)))
    except ValueError:
        messagebox.showerror('Value Error', 'Vänligen ange ett heltal som värde.')
    return False


# Errorfunktion. Testar ifall entry är en int och inte None. Skulle entry vara None betyder det att användaren inte
# tryckt på generera-knappen och därmed har entry inte fått ett int-värde tilldelat.
# Ifall entry == None öppnas ett error-meddelande med felkod.

def error_knapptryckning(entry):
    try:
        int(entry)
        return True
    except TypeError:
        messagebox.showerror('Type Error',
                             'Du måste generera värden innan du kan skapa diagram/ tabell/ textfil.')
        return False


# Funktionen sparar strängen tillhörande objektet (samma sträng som används för att öppna textfönstret) skrivs över
# till en textfil och sparas som 'ValAvKraftverkInput.txt'

def sparaText(val, entry, sträng):
    with open(val + str(entry) + '.txt', 'w+') as f:
        f.write(sträng)
    messagebox.showinfo('Textfil sparad', 'Textfilen har sparats som ' + val + str(entry) + '.txt.')


# Mainfunktion som skapar Interface-, Solkraftverk- och Vindkraftverklassen

def main():
    Gui(Solkraftverk(), Vindkraftverk())


main()
