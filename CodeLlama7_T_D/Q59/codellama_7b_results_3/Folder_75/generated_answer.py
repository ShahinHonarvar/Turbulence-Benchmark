
def all_left_truncatable_prime(tuple):
    x = tuple[41]
    list = []
    for i in range(2, x):
        if is_prime(i) and left_truncatable_prime(i):
            list.append(i)
    return sorted(list)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def left_truncatable_prime(n):

    s = str(n)

    for i in range(len(s)):

        if int(s[i]) == 0:

            break

        if not is_prime(int(s[:i] + s[i+1:]))) :

            return False

    return True
