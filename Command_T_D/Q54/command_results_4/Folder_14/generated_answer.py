def all_right_truncatable_prime(x):
    return sorted(filter(lambda n: is_right_truncatable_prime(n) and n < x, range(2, x)), reverse=True)
def is_right_truncatable_prime(n):
    return all(n % d for d in range(2, int(str(n)[-1])))
