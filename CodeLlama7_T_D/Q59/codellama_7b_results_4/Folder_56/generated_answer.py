
def all_left_truncatable_prime(tuple):
    x = tuple[30]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list.append(i)
    return sorted(list)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def is_left_truncatable_prime(n):
    if str(n)[0] == "0" or not is_prime(n):
        return False

    for i in range(1, len(str(n)))):
        if not is_prime(int(str(n))[i:])):
            return False

    return True
