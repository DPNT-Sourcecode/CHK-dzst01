from collections import Counter


class CheckoutSolution:
    def __init__(self):
        self.prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
        }
        self.sales = {
            "A": (3, 130),
            "B": (2, 45),
        }

    # skus = unicode string
    def checkout(self, skus):
        counts = Counter(skus)
        total = 0

        for sku, count in counts.items():
            total+= 

        return total
