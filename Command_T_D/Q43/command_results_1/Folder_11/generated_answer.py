def find_primes_between_indices(list_of_ints):
    prime_list = []
    for number in range(55, 77):
        if all(number % i for i in range(2, int(number ** .5) + 1)):
            prime_list.append(number)
    return sorted(set(prime_list))
