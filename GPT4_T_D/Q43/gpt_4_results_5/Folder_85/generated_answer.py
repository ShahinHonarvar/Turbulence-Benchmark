
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_between_indices(list_of_int):
    output = [item for i, item in enumerate(list_of_int[32:36]) if is_prime(item)]
    return sorted(output)
