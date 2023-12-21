
def all_left_truncatable_prime(tuple):
    x = tuple[3]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)
def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    if n == 1 or n == 0:
        return False

    while n > 1:

        if n % 10 == 0:
            n = int(n / 10)

        else:

            break


    if is_prime(n):

        return True


    else:

        return False
