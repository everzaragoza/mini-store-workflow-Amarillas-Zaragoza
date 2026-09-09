import unittest

from store import apply_discount, can_checkout, loyalty_discount, shipping_cost


class StoreTests(unittest.TestCase):
    def test_regular_shipping(self):
        self.assertEqual(shipping_cost(500), 99.0)
    def test_shipping_cost_morethan_1000(self):
        self.assertEqual(shipping_cost(1500), 0.00)

    def test_negative_subtotal_is_invalid(self):
        with self.assertRaises(ValueError):
            shipping_cost(-1)

    def test_apply_discount(self):
        self.assertEqual(apply_discount(1000, 10), 900.0)

    def test_apply_discount_invalid_percent_below_zero(self):
        with self.assertRaises(ValueError):
            apply_discount(100.0, -1)

    def test_apply_discount_invalid_percent_above_hundred(self):
        with self.assertRaises(ValueError):
            apply_discount(100.0, 101)

    def test_apply_discount_valid_boundary_percents(self):
        self.assertEqual(apply_discount(100.0, 0), 100.0)
        self.assertEqual(apply_discount(100.0, 100), 0.0)

    def test_checkout_with_items(self):
        self.assertTrue(can_checkout(1))

    def test_loyalty_starts_at_zero(self):
        self.assertEqual(loyalty_discount(0), 0)


if __name__ == "__main__":
    unittest.main()
