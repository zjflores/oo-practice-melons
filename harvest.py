############
# Part 1   #
############


class MelonType(object):
	"""A species of melon at a melon farm."""

	def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
		"""Initialize a melon."""
		self.code = code
		self.name = name
		self.first_harvest = first_harvest
		self.color = color
		self.is_seedless = is_seedless
		self.is_bestseller = is_bestseller

		self.pairings = []

		# Fill in the rest

	def add_pairing(self, pairing):
		"""Add a food pairing to the instance's pairings list."""
		self.pairings.append(pairing)

		# Fill in the rest

	def update_code(self, new_code):
		"""Replace the reporting code with the new_code."""
		self.code = new_code
		# Fill in the rest


def make_melon_types():
	"""Returns a list of current melon types."""
	all_melon_types = []

	musk = MelonType('musk', "muskmelon", 1998, 'green', True, True)
	musk.add_pairing("mint")
	all_melon_types.append(musk)

	cas = MelonType('cas', "casaba", 2003, 'orange', False, False)
	cas.add_pairing("mint")
	cas.add_pairing("strawberries")
	all_melon_types.append(cas)

	cren = MelonType('cren', "crenshaw", 1996, 'green', False, False)
	cren.add_pairing("proscuitto")
	all_melon_types.append(cren)

	yw = MelonType('yw', "yellow watermelon", 2013, 'yellow', False, True)
	yw.add_pairing("ice cream")
	all_melon_types.append(yw)
	
	return all_melon_types


melon_list = make_melon_types()


def print_pairing_info(melon_types):
	"""Prints information about each melon type's pairings."""
	for melon in melon_types:
		print("{} pairs with".format(melon.name.title()))
		for pairing in melon.pairings:
			print("- {}".format(pairing))


def make_melon_type_lookup(melon_types):
	"""Takes a list of MelonTypes and returns a dictionary of melon type by code."""
	melon_dictionary = {}
	for melon in melon_types:
		melon_dictionary[melon.code] = melon
	return melon_dictionary


############
# Part 2   #
############

class Melon(object):
	"""A melon in a melon harvest."""

	# Fill in the rest

	# Needs __init__ and is_sellable methods
	def __init__(self, melon_type, shape_rating, color_rating, field, harvested_by):
		self.type = melon_type
		self. shape_rating = shape_rating
		self.color_rating = color_rating
		self.field = field
		self.harvested_by = harvested_by

		

	def is_sellable(self):

		if self.shape_rating > 5 and self.color_rating > 5 and field != 3:
			return True
		else:
			return False



def make_melons():
	"""Returns a list of Melon objects."""

	melons = []

	Melon_1 = Melon('yw', 8, 7, 2, 'Sheila')
	melons.append(Melon_1)

	Melon_2 = Melon('yw', 3, 4, 2, 'Sheila')
	melons.append(Melon_2)

	Melon_3 = Melon('yw', 9, 8, 3, 'Sheila')
	melons.append(Melon_3)

	Melon_4 = Melon('cas', 10, 6, 35, 'Sheila')
	melons.append(Melon_4)

	Melon_5 = Melon('cren', 8, 9, 35, 'Michael')
	melons.append(Melon_5)

	Melon_6 = Melon('cren', 8, 2, 35, 'Michael')
	melons.append(Melon_6)

	Melon_7 = Melon('cren', 2, 3, 4, 'Michael')
	melons.append(Melon_7)

	Melon_8 = Melon('musk', 6, 7, 4, 'Michael')
	melons.append(Melon_8)

	Melon_9 = Melon('yw', 7, 10, 3, "Sheila")
	melons.append(Melon_9)

	return melons


melons = make_melons()


def get_sellability_report(melons):
	"""Given a list of melon object, prints whether each one is sellable."""

	for melon in melons:
		if melon.is_sellable == True:
			print("Harvested by {} from Field {} (CAN BE SOLD)".format(melon.harvested_by, melon.field))
		else:
			print("Harvested by {} from Field {} (NOT SELLABLE)".format(melon.harvested_by, melon.field))





