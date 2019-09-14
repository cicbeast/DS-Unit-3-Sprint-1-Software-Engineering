import unittest
from acme import Product
from acme_report import generate_products, adj, noun


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

    def test_steal_and_explode(self):
        """Testing the stealability and explode methods"""
        prod = Product('Test Product', 50, 25, 2.1)
        self.assertEqual(prod.stealability(),'Very Stealable!' )
        self.assertEqual(prod.explode(), '...BABOOM!!' )


if __name__ == '__main__':
    unittest.main()