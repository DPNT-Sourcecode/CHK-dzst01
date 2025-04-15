from collections import Counter


class CheckoutSolution:
    def __init__(self):
        # sku: (saleQty, salePrice)
        self.salePrices = {
            "A": [(5, 200), (3, 130), (1, 50)],
            "B": [(2, 45), (1, 30)],
            "C": [(1, 20)],
            "D": [(1, 15)],
            "E": [(1, 40)],
        }

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
        # Counts all SKUs in the skus string
        counts = Counter(skus)
        total = 0

        for sku, count in counts.items():
            try:
                for saleQty, salePrice in self.salePrices[sku]:
                    total += (count // saleQty) * salePrice
                    count %= saleQty
                    if count == 0:
                        break
            except KeyError:
                # If skus not found in prices return -1
                return -1

        return total






