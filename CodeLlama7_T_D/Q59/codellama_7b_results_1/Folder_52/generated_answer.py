
def all_left_truncatable_prime(tuple):
    x = tuple[52]
    list = []
    for i in range(1, x + 1):
        if is_prime(i) and is_left_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    if str(n)[0] == '0':
        return False

    for i in range(1, len(str(n)))):
        if int(str(n))[i:] not in [2, 3, 5, 7]:
            return False

    return True
