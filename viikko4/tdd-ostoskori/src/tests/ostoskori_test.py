import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos
class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_oikea(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        voi = Tuote("Voi", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(voi)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_oikea(self):
        maito = Tuote("Maito", 3)
        voi = Tuote("Voi", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(voi)
        self.assertEqual(self.kori.hinta(), 4)
    

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
       
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_oikea(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertAlmostEqual(type(ostokset[0]) is type(Ostos(maito)), True)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuote.nimi(), "Maito")
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        voi = Tuote("Voi", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(voi)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
        self.assertEqual(type(ostokset[0]) is type(Ostos(maito)), True)
        self.assertEqual(type(ostokset[1]) is type(Ostos(voi)), True)
    
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(type(ostokset[0]) is type(Ostos(maito)), True)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostos_jossa_on_oikea_lukumaara(self):
        maito = Tuote("Maito", 3)
       
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostos_jossa_on_oikea_nimi(self):
        maito = Tuote("Maito", 3)
       
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].tuote.nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_jos_korissa_on_kaksi_samaa_tuotetta_ja_toinen_poistetaan_on_ostoksen_maara_oikea(self):
        maito = Tuote("Maito", 3)
       
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(ostokset[0].lukumaara(), 1)
    
    def test_jos_korissa_on_yksi_tuotet_ja_tuote_poistetaan_on_kori_tyhja(self):
        maito = Tuote("Maito", 3)
       
        
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
       
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        
        

