def all_left_truncatable_prime(n):
    return sorted(list(filter(left_truncatable_prime, range(2, n[20] + 1))), reverse=True)
def left_truncatable_prime(n):
    # Your code here.
    return all(a % 10 == b for a, b in zip(str(n), range(10)))
