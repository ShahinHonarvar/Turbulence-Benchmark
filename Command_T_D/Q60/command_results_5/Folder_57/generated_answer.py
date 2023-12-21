
def all_left_right_truncatable_prime(num_range):
    res = []
    for n in range(2, num_range[0] + 1):
        if n == 2 or n == 3:
            res.append(n)
        elif n % 2 == 0 or n % 3 == 0:
            res.append(n)
        elif n % 5 == 0:
            res.append(n)
        elif n % 10 == 0:
            res.append(n)
        elif n % 100 == 0:
            res.append(n)
        elif n % 1000 == 0:
            res.append(n)
    return res
