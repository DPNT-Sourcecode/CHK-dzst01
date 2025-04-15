from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    def test_checkout(self):
        assert CheckoutSolution().checkout("AAABB") == 175
        assert CheckoutSolution().checkout("AABCD") == 165
        assert CheckoutSolution().checkout("AAAA") == 180
        assert CheckoutSolution().checkout("AAAAA") == 200
        assert CheckoutSolution().checkout("AAAAAAAA") == 330
        assert CheckoutSolution().checkout("EE") == 80
        assert CheckoutSolution().checkout("hello") == -1
        assert CheckoutSolution().checkout("") == 0


