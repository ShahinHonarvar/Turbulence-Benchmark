import itertools
def all_right_truncatable_prime(n):
    return sorted(filter(lambda x: is_right_truncatable_prime(x) and x < n[70], 
                     itertools.permutations(range(3, n[70] + 1, 2)))), reverse=True)
def is_right_truncatable_prime(x):
    x += 1
    while x > 9:
        x //= 10
    return x > 1
