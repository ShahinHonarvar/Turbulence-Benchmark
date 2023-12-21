def all_right_truncatable_prime(n):
    return sorted(filter(lambda x: is_right_truncatable_prime(x) and x < n[31], range(3, n[31] + 1)), reverse=True)
def is_right_truncatable_prime(n):
    return all(n % d == 0 for d in range(2, int(n ** .5) + 1))
