
import unittest

from Homework_07 import funciones

f = funciones([1,2,2,4,4,5,6,7,7,7,"hola"])

class Prueba_errores(unittest.TestCase):
    def test_creacion(self):
        self.assertRaises(ValueError, funciones, "hola")
    
    def test_creacionf(self):
        self.assertEqual(f.lista, [1,2,2,4,4,5,6,7,7,7,"hola"])

    def test_primo(self):
        self.assertCountEqual(f.primo(), [False, True, True, False, False, True, False, True, True, True, False])
        self.assertCountEqual(f.rep(1), [7, 3])




#if __name__ == "__main__":
#    unittest.main()

unittest.main(argv=[""], verbosity=2, exit=False)