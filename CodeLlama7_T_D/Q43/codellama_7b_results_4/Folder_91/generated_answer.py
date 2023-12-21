
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(len(my_list)):
        if is_prime(i, my_list):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n, my_list):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
