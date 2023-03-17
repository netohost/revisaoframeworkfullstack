import unittest
import requests

class Teste(unittest.TestCase):

    def test_00_media(self):
        r1 = requests.get("http://localhost:5000/?nota1=6&nota2=7")
        if "6.5" not in r1.text:
            self.fail("média de 6 com 7 deve dar 6.5")

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Teste)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

runTests()