
def all_right_truncatable_prime(tuple):
    x = tuple[88]
    prime_numbers = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):
    digits = len(str(n)) - 1

    for i in range(digits, -1, -1):
        if str(n)[i] == "0":
            return False

    return True
