from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = {}
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self.kori.values())
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.kori.values())
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if(lisattava.nimi() not in self.kori):
            ostos = Ostos(lisattava)
            self.kori[ostos.tuote.nimi()] = ostos
        else:
            self.kori[lisattava.nimi()].muuta_lukumaaraa(1)



    def poista_tuote(self, poistettava: Tuote):
        if(poistettava.nimi() in self.kori):
            self.kori[poistettava.nimi()].muuta_lukumaaraa(-1)
            if(self.kori[poistettava.nimi()].lukumaara() <= 0):
                self.kori.pop(poistettava.nimi())
            

        

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self.kori.values())
        
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
