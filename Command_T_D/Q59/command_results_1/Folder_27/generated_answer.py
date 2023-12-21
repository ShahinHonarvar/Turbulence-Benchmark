def all_left_truncatable_prime(a):
    x = a[79]
    return sorted(list(range(2, x)), key=lambda i: str(i))
