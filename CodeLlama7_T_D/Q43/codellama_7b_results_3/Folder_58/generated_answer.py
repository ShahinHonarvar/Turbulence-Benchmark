
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(157, 736):
        if my_list[i] == 1:
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
