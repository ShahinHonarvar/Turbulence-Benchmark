
def all_left_truncatable_prime(tuple):
    x = tuple[992]
    list = []
    for i in range(1, x):
        if is_prime(i) and left_truncatable_prime(i):
            list.append(i)
    return sorted(list)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def left_truncatable_prime(n):
    while n > 1:
        if str(n)[0] != '2' and str(n)[0] != '3' and str(n)[0] != '5':
            return False

        n = int(str(n)[:-1]))

    return True
