
import itertools

def all_left_right_truncatable_prime(n):
    return [i for i in range(2, n[0] + 1) if all(str(i) for j in range(2, int(str(i)[0]) + 1) if str(i)[:j] + str(i)[-j:]]
