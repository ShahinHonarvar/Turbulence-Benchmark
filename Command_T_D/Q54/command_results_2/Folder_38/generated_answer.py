import itertools
def all_right_truncatable_prime(n):
    return sorted(list(filter(lambda x: is_right_truncatable_prime(x), list(range(2, int(str(n)[-1])+1)))), key=lambda x: x)
def is_right_truncatable_prime(x):
    for c in str(x)[-1::-1]:
        if x % int(c) == 0:
            return False
    return True
