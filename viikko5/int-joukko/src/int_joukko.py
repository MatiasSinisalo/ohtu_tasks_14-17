KAPASITEETTI = 5
OLETUSKASVATUS = 5

#luokassa on siirrytty käyttämään normaalia pythonin taulua, koska viikko 5 tehtävässä 6 mainittiin monimutkaisuuden vähentäminen.
class IntJoukko:
    def __init__(self, kapasiteetti:int=KAPASITEETTI, kasvatuskoko:int=OLETUSKASVATUS):
        if kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        self.kasvatuskoko = kasvatuskoko

        self.ljono = []

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono
        

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono.append(n)
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        else:
            return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    
    def alkoita_joukossa(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return list(self.ljono)

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        yhdiste = a_taulu + b_taulu

        for i in range(0, len(yhdiste)):
            x.lisaa(yhdiste[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            if a_taulu[i] in b_taulu:
                 y.lisaa(a_taulu[i])
            

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            if a_taulu[i] not in b_taulu:
                z.lisaa(a_taulu[i])

      

        return z

    def __str__(self):
       tulostus = "{" + str(self.ljono) + "}"
       tulostus = tulostus.replace("[", "")
       tulostus = tulostus.replace("]", "")
       return tulostus
