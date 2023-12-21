def all_right_truncatable_prime(x):
    return sorted(filter(right_truncatable_prime, range(2, x)), reverse=True)
def right_truncatable_prime(n):
    return all(str(n).endswith(d) for d in range(2, str(n)[-1] + 1))
