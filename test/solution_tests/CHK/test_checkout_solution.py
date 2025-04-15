from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    def test_checkout(self):
        assert CheckoutSolution().checkout("AAABB") == 175
        assert CheckoutSolution().checkout("AABCD") == 165
        assert CheckoutSolution().checkout("AAAA") == 180


