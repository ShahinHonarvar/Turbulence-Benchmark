
def all_left_truncatable_prime(tuple):
    x = tuple[73]
    left_truncatable_prime_numbers = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            left_truncatable_prime_numbers.append(i)
    return sorted(left_truncatable_prime_numbers, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    if n < 2:
        return False

    for i in range(len(str(n)) - 1, 0, -1):
        if not is_prime(int(str(n)[i:] + str(n)[0:i])):
            return False

    return True
