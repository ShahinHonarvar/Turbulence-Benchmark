
def all_left_truncatable_prime(tuple):
    x = tuple[73]
    list_of_all_ltpns = []
    for i in range(2, x):
        if is_prime(i) and left_truncation_is_prime(i):
            list_of_all_ltpns.append(i)
    return sorted(list_of_all_ltpns, reverse=True)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def left_truncation_is_prime(n):
    while n > 1:
        n //= 10

    return is_prime(n)
