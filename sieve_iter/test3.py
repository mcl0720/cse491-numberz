import sieve

def test3():
    s = sieve.sieve()
    i = iter(s)
    for x in range(15):
	i.next()
    assert i.next() == 59 # the seventeenth prime number should be 59
    
test3()