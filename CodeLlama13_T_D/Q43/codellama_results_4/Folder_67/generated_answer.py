
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(17, 80):
        if my_list[i] not in prime_numbers:
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers, reverse=True)
