import sys
def all_right_truncatable_prime(test_tup):
    for e in test_tup:
        if e == 0:
            break
        else:
            yield from [str(n) for n in range(2, int(e ** .5) + 1) if all(str(n) in str(i) for i in range(2, int(n ** .5) + 1) if i == n or i == 1)]
