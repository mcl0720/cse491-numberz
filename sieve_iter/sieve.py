# this is an implementation of Eratosthenes' Sieve using
# Python's iterator functionality.  Here, 'sieve' is a class that
# obeys the iterator protocol.

class sieve(object):
    def __init__(self):
        self.primeslist = [2]

    def __iter__(self):
        return self

    def next(self):
        start = self.primeslist[-1] + 1
	while 1:
	    if self.is_prime(start):
		self.primeslist.append(start)
		return start

	    start += 1
	    
    def is_prime(self, n):
	for i in self.primeslist:
	    if n % i == 0:
		return False
	return True
