from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Toiminto:
    def __init__(self, komento, arvo_ennen):
        self.komento = komento
        self.arvo_ennen = arvo_ennen


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        #lista sisältäen menneet Toiminnot eli komento, arvo_ennen parit
        self.historia = []
        self.komennot = {
            Komento.SUMMA : lambda arvo: self.Summa(sovellus, arvo),
            Komento.EROTUS : lambda arvo: self.Erotus(sovellus, arvo),
            Komento.NOLLAUS : lambda arvo: self.Nollaus(sovellus, arvo),  
            Komento.KUMOA : lambda arvo: self.Kumoa(sovellus, arvo),  
        }

    def Summa(self, sovellus, arvo):
        self.historia.append(Toiminto(Komento.SUMMA, sovellus.tulos))
        sovellus.plus(arvo)

    def Erotus(self, sovellus, arvo):
        self.historia.append(Toiminto(Komento.EROTUS, sovellus.tulos))
        sovellus.miinus(arvo)
    
    def Nollaus(self, sovellus, arvo):
        self.historia.append(Toiminto(Komento.NOLLAUS, sovellus.tulos))
        sovellus.nollaa()
    
    def Kumoa(self, sovellus, arvo):
        if len(self.historia)> 0:
            edellinen_toiminto = self.historia.pop()
            sovellus.aseta_arvo(edellinen_toiminto.arvo_ennen)
        else:
            self._kumoa_painike["state"] = constants.DISABLED

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        arvo = 0
        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass
        return arvo

    def _suorita_komento(self, komento):
        self._kumoa_painike["state"] = constants.NORMAL

        if komento in self.komennot:
            self.komennot[komento](self._lue_syote())

        

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)
