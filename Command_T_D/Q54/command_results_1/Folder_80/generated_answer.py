import itertools
def all_right_truncatable_prime(test_tup):
    # type: (tuple) -> list
    for n in range(10, int(test_tup[14])+1):
        if all(str(n) in str(m) for m in range(10, n//2)):
            yield from itertools.takewhile(lambda x: x%10!=0, n)
