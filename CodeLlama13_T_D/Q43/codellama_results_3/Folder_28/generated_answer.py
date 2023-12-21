
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(38, 55):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers, reverse=True)
