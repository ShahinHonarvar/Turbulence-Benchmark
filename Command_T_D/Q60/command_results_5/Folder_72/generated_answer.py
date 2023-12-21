
import itertools

def all_left_right_truncatable_prime(n):
    return [p for p in itertools.permutations(str(p)) if all(p%10==i for i in range(10)) and p in range(2,n+1)]
