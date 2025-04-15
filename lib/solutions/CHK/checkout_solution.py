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
			"H": [(5, 45), (10,80), (1, 10)],  
			"I": [(1, 35)],
			"J": [(1, 60)],  
			"K": [(1, 80)],    | 2K for 150             |
			"L": [(1, 90)],
			"M": [(1, 15)], 
			"N": [(1, 40)],    | 3N get one M free      |
			"O": [(1, 10)],
			"P": [(5, 200), (1, 50)],    |              |
			"Q": [(3Q for 80)(1, 30)],    | 3Q for 80              |
			"R": [(1, 50)],    | 3R get one Q free      |
			"S": [(1, 30)],  
			"T": [(1, 20)],  
			"U": [(1, 40)],    | 3U get one U free      |
			"V": [(1, 50)],    | 2V for 90, 3V for 130  |
			"W": [(1, 20)],
			"X": [(1, 90)],
			"Y": [(1, 10)],
			"Z": [(1, 50)],
		}

		self.freeItems = {
			"E": [("B", 2)],
			"F": [("F", 3)],
		}

	# skus = unicode string
	def checkout(self, skus):
		# If not a string
		if not isinstance(skus, str):
			return -1

		# Counts all SKUs in the skus string
		counts = Counter(skus)

		try:
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
