class Mediant(object):

	numerator = None
	denominator = None
	
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator
		
	def to_string(self):
		return str(self.numerator) + '/' + str(self.denominator)
