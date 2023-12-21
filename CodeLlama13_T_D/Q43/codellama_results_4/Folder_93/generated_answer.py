
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(70, 71):
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0:
            continue
        else:
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers, reverse=True)
