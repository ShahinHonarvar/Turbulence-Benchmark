
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(239, 686+1):
        if my_list[i] not in prime_numbers and is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers)
