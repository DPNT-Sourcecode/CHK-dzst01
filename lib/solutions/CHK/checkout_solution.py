from collections import Counter


class CheckoutSolution:
    def __init__(self):
        self.prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
        }
        # sku: (saleQty, salePrice)
        self.salePrices = {
            "A": (3, 130),
            "B": (2, 45),
        }

    # skus = unicode string
    def checkout(self, skus):
        # Caunts all SKUs in the skus string
        counts = Counter(skus)
        total = 0

        for sku, count in counts.items():
            price = self.prices[sku]
            if sku in self.salePrices:
                saleQty, salePrice = self.salePrices[sku]
                # Find number of sale
                total += (count // saleQty) * salePrice + (count % saleQty) * price
            else:
                total += count * price

        return total




