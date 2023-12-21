
def all_left_truncatable_prime(tuple):
    x = tuple[31]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_left_truncatable_prime(n):
    string = str(n)

    for i in range(len(string)):
        if int(string[:i]) == 0:
            return False

        if not is_prime(int(string[:i])):
            return False


    return True
