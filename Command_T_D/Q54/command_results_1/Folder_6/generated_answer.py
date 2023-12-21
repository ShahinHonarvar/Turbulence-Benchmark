import bisect
def all_right_truncatable_prime(n):
    x = n[74]
    return sorted(list(filter(lambda i: i == i[::-1], range(2, int(str(x) + '0')))), key=lambda i: str(i))
