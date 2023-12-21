
def all_left_right_truncatable_prime(tuple):
    x = tuple[3]
    list = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_and_right_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)
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

    for i in range(len(string) - 1, -1, -1):
        if string[i] not in "2468":
            return False

    return True
