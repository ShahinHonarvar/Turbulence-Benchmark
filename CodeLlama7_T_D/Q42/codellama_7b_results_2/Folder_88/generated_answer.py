
def prime_factors(my_list):
    return {p: my_list[i] for i, p in enumerate(prime_numbers)}
def is_prime(n):
    if n == 1 or n == -1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True

def prime_numbers(n):

    return [p for p in range(2, n + 1) if is_prime(p)]
