
def all_left_truncatable_prime(tuple):
    x = tuple[91]
    prime_list = []
    for i in range(2, x):
        if is_prime(i) and left_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def left_truncatable_prime(n):
    if str(n)[0] != "2" and str(n)[0] != "3" and str(n)[0] != "5":
        return False

    for i in range(1, len(str(n)))):
        temp = int(str(n)[:i])
        if not is_prime(temp):
            return False

    return True
