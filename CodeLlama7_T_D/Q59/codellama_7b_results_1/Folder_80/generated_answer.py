
def all_left_truncatable_prime(tuple):
    x = tuple[14]
    list = []
    for i in range(2,x):
        if is_prime(i) and left_truncatable(i):
            list.append(i)
    return sorted(list, reverse=True)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True


def left_truncatable(n):

    s = str(n)

    for i in range(len(s)):

        num = int(s[:-i])

        if not is_prime(num):

            return False

    return True
