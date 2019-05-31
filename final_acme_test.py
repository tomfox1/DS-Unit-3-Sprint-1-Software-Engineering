import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS




class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_weight(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_explode(self):
        """Test default explode function works"""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')

    def test_stealability(self):
        """Test default stealability function works"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'very stealable')

class AcmeReportTests(unittest.TestCase):
    
    def test_default_num_products(self):
        """Test default n. projects equals 30"""
        val = generate_products()
        self.assertEqual(len(val), 30)

     
      


if __name__ == '__main__':
    unittest.main()