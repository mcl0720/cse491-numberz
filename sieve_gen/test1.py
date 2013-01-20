import sieve

def test1():
    s = sieve.sieve()
    i = iter(s)
    assert i.next() == 3
    
test1()