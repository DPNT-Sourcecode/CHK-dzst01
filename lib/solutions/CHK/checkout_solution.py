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
            "F": [(1, 10)],
            "G": [(1, 20)],
            "H": [(10, 80), (5, 45), (1, 10)],
            "I": [(1, 35)],
            "J": [(1, 60)],
            "K": [(2, 150), (1, 70)],
            "L": [(1, 90)],
            "M": [(1, 15)],
            "N": [(1, 40)],
            "O": [(1, 10)],
            "P": [(5, 200), (1, 50)],
            "Q": [(3, 80), (1, 30)],
            "R": [(1, 50)],
            "S": [(1, 20)],
            "T": [(1, 20)],
            "U": [(1, 40)],
            "V": [(3, 130), (2, 90), (1, 50)],
            "W": [(1, 20)],
            "X": [(1, 17)],
            "Y": [(1, 20)],
            "Z": [(1, 21)],
        }

        self.freeItems = {
            "E": [("B", 2)],
            "F": [("F", 3)],
            "N": [("M", 3)],
            "R": [("Q", 3)],
            "U": [("U", 4)],
        }

        self.groups = [("STXYZ", 3, 45)]

    # skus = unicode string
    def checkout(self, skus):
        # If not a string
        if not isinstance(skus, str):
            return -1

        # Counts all SKUs in the skus string
        counts = Counter(skus)

        try:
            for groupItems, groupSize, groupPrice:
                group

            for sku, freeItemsList in self.freeItems.items():
                for freeSku, saleQty in freeItemsList:
                    counts[freeSku] -= counts[sku] // saleQty

            total = 0
            for sku, count in counts.items():
                for saleQty, salePrice in self.salePrices[sku]:
                    if count <= 0:
                        break
                    total += (count // saleQty) * salePrice
                    count %= saleQty

        except KeyError:
            # If skus not found in prices return -1
            return -1

        return total





