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

        self.freeItems = {
            "E": [("B", 2)],
        }

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
        # Counts all SKUs in the skus string
        counts = Counter(skus)

        for sku, freeItemsList in self.freeItems.items():
            for freeSku, saleQty in freeItemsList:
                counts[freeSku] -= counts[sku] % saleQty

        total = 0
        for sku, count in counts.items():
            try:
                for saleQty, salePrice in self.salePrices[sku]:
                    if count <= 0:
                        break
                    total += (count // saleQty) * salePrice
                    count %= saleQty
            except KeyError:
                # If skus not found in prices return -1
                return -1

        return total
