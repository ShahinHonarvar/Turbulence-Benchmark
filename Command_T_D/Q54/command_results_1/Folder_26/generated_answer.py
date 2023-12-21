import sys
def all_right_truncatable_prime(tup):
    return [i for i in range(1, tup[81]) if is_right_truncatable_prime(i)]
def is_right_truncatable_prime(x):
    return all(x%i == 0 or x%i == 1 for i in range(2, int(str(x)[-1])))
