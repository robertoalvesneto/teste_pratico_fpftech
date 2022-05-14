import unittest
from vanitonpages.triangle import Triangle


class TestTriangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.website_url = "http://www.vanilton.net/triangulo/#"
        cls.t = Triangle()
        cls.t.start_firefox_driver()

        cls.default_text = "Digite os valores dos vértices do triângulo para identificar o seu tipo"
        cls.error_message = "Erro"
        cls.eq = "Equilátero"
        cls.esc = "Escaleno"
        cls.iso = "Isósceles"

    @classmethod
    def setDownClass(cls):
        cls.t.stop_driver()

    def setUp(self):
        self.t.open_page(self.website_url)

    def test_equilatero(self):
        input_text = [2.0, 2.0, 2]
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.eq)
    
    def test_escaleno(self):
        input_text = [0.1, 200, 1.2]
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.esc)
    
    def test_isosceles(self):
        input_text = [3, 2.0, 2]
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.iso)
    
    def test_invalid_sizes(self):
        input_text = [5, 2, 1]
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.error_message)
    
    def test_zero_size(self):
        input_text = [1, 2, 0]
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.error_message)
    
    def test_less_size(self):
        input_text = [1, 2, -2]
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.error_message)

    def test_empty(self):
        input_text = [1, 2, '']
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.default_text)
    
    def test_text(self):
        input_text = [1, 2, 'a']
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.error_message)
    
    def test_null(self):
        input_text = [1, 2, 'null']
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.error_message)
    
    def test_not_a_number(self):
        input_text = [1, 2, 'NaN']
        self.t.set_input_fields(input_text)
        text = self.t.get_body_last_value()

        self.assertIn(text, self.error_message)

if __name__ == "__main__":
    # rodar os testes:
    # python3 -m tests.gc_textfield_test
    unittest.main()