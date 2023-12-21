
def all_right_truncatable_prime(tuple):
    x = tuple[429]
    prime_numbers = []
    for i in range(10, x):
        if is_prime(i) and is_right_truncatable_prime(i, x):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
def is_prime(n):
    for i in range(2, int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n, x):
    while n > 9 and n < x:
        if str(n)[-1] != '1' and str(n)[-1] != '3' and str(n)[-1] != '7':
            return False

        n = int(str(n)[:-1])

    return True
