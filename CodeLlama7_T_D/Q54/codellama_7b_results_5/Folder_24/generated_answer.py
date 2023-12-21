
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[65]
    list_of_all_rtp = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            list_of_all_rtp.append(i)
    return sorted(list_of_all_rtp, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    for i in range(len(str(n))) - 1, len(str(n)) - 1, -1:
        if not is_prime(int(str(n)[i:] + str(n)[:i])):
            return False

    return True
