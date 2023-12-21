
def find_primes_between_indices(my_list):
    # Find all prime numbers between indices 20 and 48, both inclusive
    prime_numbers = []
    for i in range(20, 49):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers, reverse=True)
