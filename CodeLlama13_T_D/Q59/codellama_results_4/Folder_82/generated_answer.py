
def all_left_truncatable_prime(x):
    x = tuple(x)
    return sorted([i for i in range(10**69) if is_left_truncatable_prime(i, x[69])], reverse=True)

def is_left_truncatable_prime(n, x):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(x**0.5)):
        if n % i == 0:
            return False
    return True
