def all_left_truncatable_prime(a):
    return sorted(
        (x for x in range(2, a[77]) if all(x % i for i in range(2, int(str(x)[0])))
    )
