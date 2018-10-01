'''This program prints all prime numbers up to a given value. '''

class Number(object):
	prime = True
	def __init__(self, value):
		self.value = value
	def isPrime(self):
		for i in range(2, self.value):
			if self.value % i == 0:
				self.prime = False
		return self.prime


def Run_Program():
	value = raw_input('Enter a value greater than 1 or X to exit: ')
	value = value.upper()
	if value == 'X':
		global start
		start = False
	elif int(value) <= 1:
		print 'Value is invalid'
	else:
		for i in range (2, int(value)):
			current_value = Number(i)
			if current_value.isPrime() == True:
				print current_value.value


start = True
while start == True:
	Run_Program() 

