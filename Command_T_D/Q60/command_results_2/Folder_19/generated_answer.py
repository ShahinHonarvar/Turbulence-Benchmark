
def all_left_right_truncatable_prime(x):
    return sorted(filter(left_right_truncatable_prime, range(2, x)), reverse=True)

def left_right_truncatable_prime(n):
    prime = True
    while n % 2 == 0 or n % 3 == 0:
        n /= 2
        prime = True
    if n == 1:
        return True
    return all(left_right_truncatable_prime(n) for i in range(5, n // 2 + 1) if n % i == 0)
