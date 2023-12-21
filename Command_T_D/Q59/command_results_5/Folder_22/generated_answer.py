def all_left_truncatable_prime(n):
    return sorted(list(filter(lambda x: is_left_truncatable_prime(x), range(2, n[85]))))
def is_left_truncatable_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = str(n)
    while d:
        if int(d[0]) == 0:
            return False
        d = d[1:]
    return True
