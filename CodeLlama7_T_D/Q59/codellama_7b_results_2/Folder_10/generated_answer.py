
def all_left_truncatable_prime(tuple):
    x = tuple[38]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i, x):
            list.append(i)
    return sorted(list, reverse=True)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def is_left_truncatable_prime(n, x):
    if n < 2 or n > x - 1:
        return False

    if str(n)[-1] != '1':
        return False

    for i in range(len(str(n)) - 2, -1, -1):
        num = int(str(n)[:i + 1])
        if not is_prime(num):
            return False

    return True
