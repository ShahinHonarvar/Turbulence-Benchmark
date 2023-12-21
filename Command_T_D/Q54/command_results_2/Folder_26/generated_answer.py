def all_right_truncatable_prime(x):
    l = []
    for i in range(2, x):
        if is_prime(i):
            j = str(i)
            while j[-1] == '0':
                j = int(j[0:-1])
            if is_prime(j):
                l.append(j)
    return sorted(l, reverse=True)
def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
