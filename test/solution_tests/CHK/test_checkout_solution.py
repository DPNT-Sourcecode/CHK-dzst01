from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    def test_checkout(self):
        assert CheckoutSolution().checkout("AAABB") == 175
        assert CheckoutSolution().checkout("AABCD") == 165
        assert CheckoutSolution().checkout("AAAA") == 180
        assert CheckoutSolution().checkout("AAAAA") == 200
        assert CheckoutSolution().checkout("AAAAAAAA") == 330
        assert CheckoutSolution().checkout("EEB") == 80
        assert CheckoutSolution().checkout("EEEB") == 120
        assert CheckoutSolution().checkout("EEEEB") == 160
        assert CheckoutSolution().checkout("EEEEBB") == 160
        assert CheckoutSolution().checkout("hello") == -1
        assert CheckoutSolution().checkout(2234) == -1
