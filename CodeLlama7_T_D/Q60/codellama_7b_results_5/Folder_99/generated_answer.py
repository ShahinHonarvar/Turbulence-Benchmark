
def all_left_right_truncatable_prime(tuple):
    x = tuple[758]
    list = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_and_right_truncatable_prime(i):
            list.append(i)
    return sorted(list)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_left_and_right_truncatable_prime(n):
    string = str(n)

    for i in range(len(string)):
        if string[i] == "0":
            return False


    left = int(string[:-1])

    right = int(string[1:])

    if is_prime(left) and is_prime(right):
        return True


    return False
