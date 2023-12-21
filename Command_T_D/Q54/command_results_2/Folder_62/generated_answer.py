def all_right_truncatable_prime(a):
    n = int(a[70])
    return sorted(filter(
        lambda x: x.is_prime()
        and x.is_right_truncatable(),
        range(2, n),
    )))
