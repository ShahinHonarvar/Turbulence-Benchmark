
import itertools

def all_left_right_truncatable_prime(test_tup):
    # input: test_tup = (x)
    # output: [] or [int]
    # return list of left-and-right-truncatable prime numbers less than or equal to x
    # delimiting done in the function
    return sorted(list(set(map(str, (p for p in itertools.permutations(str(test_tup[8]) if p.isPrime()))))), reverse=True)
