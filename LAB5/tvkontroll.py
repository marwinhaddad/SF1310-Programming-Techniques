class Tv:

    def __init__(self, namntv, kanalmax, kanal, ljudmax, ljud):
        self.namntv = namntv
        self.kanalmax = int(kanalmax)
        self.kanal = int(kanal)
        self.ljudmax = int(ljudmax)
        self.ljud = int(ljud)

    def ljudupp(self):
        if self.ljud < self.ljudmax:
            self.ljud += 1
            return self.ljud
        else:
            return self.ljud

    def ljudner(self):
        if self.ljud > 0:
            self.ljud -= 1
            return self.ljud
        else:
            return self.ljud

    def kanal(self, kanalnr):
        self.kanal = kanalnr

    def tvmeny(self):
        return self.namntv+"\n"+"kanal: "+str(self.kanal)+"\n"+"Volym: "+str(self.ljud)