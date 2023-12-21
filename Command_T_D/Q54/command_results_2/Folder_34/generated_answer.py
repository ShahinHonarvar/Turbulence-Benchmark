def all_right_truncatable_prime(tup):
    res = []
    for n in range(2, tup[18] + 1):
        is_prime = True
        while n:
            if n % 2 == 0:
                is_prime = False
                break
            n //= 2
        if is_prime:
            res += [n]
    return res
