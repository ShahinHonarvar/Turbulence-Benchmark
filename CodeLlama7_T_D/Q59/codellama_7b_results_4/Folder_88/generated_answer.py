
def all_left_truncatable_prime(tuple):
    x = tuple[93]
    list = []
    for i in range(2, x):
        if is_prime(i) and left_truncatable_prime(i):
            list.append(i)
    return sorted(list)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    while n > 0:
        if n % 10 == 0:
            return False
        n = int(str(n)[:-1])
    return True
