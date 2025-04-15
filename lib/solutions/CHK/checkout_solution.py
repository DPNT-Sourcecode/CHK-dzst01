from collections import Counter


class CheckoutSolution:
    def __init__(self):
        self.prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
        }
        # sku: (saleQty, salePrice)
        self.salePrices = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
        }

    # skus = unicode string
    def checkout(self, skus):
        # Counts all SKUs in the skus string
        counts = Counter(skus)
        total = 0

        for sku, count in counts.items():
            try:
                price = self.prices[sku]
                if sku in self.salePrices:
                    saleQty, salePrice = self.salePrices[sku]
                    # Find number of sale items and price and add remain items as normal
                    total += (count // saleQty) * salePrice + (count % saleQty) * price
                else:
                    total += count * price
            except KeyError:
                # If skus not found in prices return -1
                return -1

        return total

