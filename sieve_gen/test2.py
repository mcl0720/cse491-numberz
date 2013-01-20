import sieve

def test2():
    s = sieve.sieve()
    i = iter(s)
    
    for x in range(3):
	i.next()

    assert i.next() == 11 # the fifth prime number should be 11
    
test2()