import contextlib
import io
import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_add_dvd_success(self):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc("Dune", cost=10)))
        self.assertEqual(len(cart.items), 1)

    def test_add_dvd_until_full(self):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            for number in range(MAX_NUMBERS_ORDERED):
                self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {number}")))
            self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_remove_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Dune")
        with contextlib.redirect_stdout(io.StringIO()):
            cart.add_dvd(dvd)
            self.assertTrue(cart.remove_dvd(dvd))
        self.assertEqual(cart.items, [])

    def test_discounted_total(self):
        cart = Cart()
        cart.items = [DigitalVideoDisc("A", cost=40), DigitalVideoDisc("B", cost=60)]
        self.assertEqual(cart.total_cost_with_discount(20), 80)

    def test_discount_percent_must_be_valid(self):
        cart = Cart()
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        cart = Cart()
        cart.items = [DigitalVideoDisc("Star Wars"), DigitalVideoDisc("Aladdin")]
        self.assertEqual([dvd.title for dvd in cart.sort_by_title()], ["Aladdin", "Star Wars"])

    def test_sort_by_cost(self):
        cart = Cart()
        cart.items = [DigitalVideoDisc("B", cost=20), DigitalVideoDisc("A", cost=10)]
        self.assertEqual([dvd.title for dvd in cart.sort_by_cost()], ["A", "B"])

    def test_print_empty_cart(self):
        cart = Cart()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            cart.print_cart()
        self.assertIn("The cart is empty", output.getvalue())


if __name__ == "__main__":
    unittest.main()
