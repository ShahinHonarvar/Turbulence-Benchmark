
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(13, 69):
        if my_list[i] == 2 or my_list[i] % 2 != 0:
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers)
