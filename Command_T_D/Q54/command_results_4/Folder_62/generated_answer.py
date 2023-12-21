import sys
def all_right_truncatable_prime(tup):
    tup = sorted(tup)
    max_n = tup[-1]
    n = max_n - 1
    result = []
    while n > 1:
        if all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            result.append(n)
            break
        n -= 1
    return result
