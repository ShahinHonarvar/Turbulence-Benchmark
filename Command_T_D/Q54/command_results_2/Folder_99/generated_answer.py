import itertools
def all_right_truncatable_prime(n):
    # your code here
    x = n[758]
    return sorted(filter(lambda x: all(str(x) in '0123456789' for _ in range(len(str(x)))), filter(lambda x: x.is_prime(), itertools.permutations(str(x)))), key=lambda x: x)
