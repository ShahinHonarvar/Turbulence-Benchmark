def all_right_truncatable_prime(n):
    i = 29
    res = []
    while i < n[0]:
        if is_prime(i):
            res += [i]
            i += 1
        i = i // 10
    return res
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
