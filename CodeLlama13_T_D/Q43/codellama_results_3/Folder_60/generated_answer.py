
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(46, 85 + 1):
        if my_list[i] % 2 == 0 and my_list[i] != 2:
            continue
        else:
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers)
