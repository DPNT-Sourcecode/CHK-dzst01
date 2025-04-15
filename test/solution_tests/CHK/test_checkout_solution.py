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
        assert CheckoutSolution().checkout("EEEEB") == 160
        assert CheckoutSolution().checkout("FFF") == 20
        assert CheckoutSolution().checkout("FFFF") == 30
        assert CheckoutSolution().checkout("FFFFFF") == 40
        assert CheckoutSolution().checkout("G") == 20
        assert CheckoutSolution().checkout("H") == 10
        assert CheckoutSolution().checkout("I") == 35
        assert CheckoutSolution().checkout("J") == 60
        assert CheckoutSolution().checkout("K") == 70
        assert CheckoutSolution().checkout("KK") == 120
        assert CheckoutSolution().checkout("L") == 90
        assert CheckoutSolution().checkout("M") == 15
        assert CheckoutSolution().checkout("N") == 40
        assert CheckoutSolution().checkout("NNNM") == 120
        assert CheckoutSolution().checkout("O") == 10
        assert CheckoutSolution().checkout("P") == 50
        assert CheckoutSolution().checkout("PPPPP") == 200
        assert CheckoutSolution().checkout("Q") == 30
        assert CheckoutSolution().checkout("R") == 50
        assert CheckoutSolution().checkout("RRRQ") == 150
        assert CheckoutSolution().checkout("S") == 20
        assert CheckoutSolution().checkout("T") == 20
        assert CheckoutSolution().checkout("U") == 40
        assert CheckoutSolution().checkout("UUUU") == 120
        assert CheckoutSolution().checkout("V") == 50
        assert CheckoutSolution().checkout("VVV") == 130
        assert CheckoutSolution().checkout("W") == 20
        assert CheckoutSolution().checkout("X") == 17
        assert CheckoutSolution().checkout("Y") == 20
        assert CheckoutSolution().checkout("Z") == 21
        assert CheckoutSolution().checkout("STXYZ") == 45
        assert CheckoutSolution().checkout("SSSSS") == 45
        assert CheckoutSolution().checkout("ZZTTT") == 45
        assert CheckoutSolution().checkout("ZZTTTSSSYY") == 90
        assert CheckoutSolution().checkout("XXXXXXXXXX") == 90
        assert CheckoutSolution().checkout("XXXZZZ") == 62
        assert CheckoutSolution().checkout("hello") == -1
        assert CheckoutSolution().checkout(2234) == -1


