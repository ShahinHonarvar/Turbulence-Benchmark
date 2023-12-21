
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(13, 29+1):
        if my_list[i] == 0:
            continue
        elif my_list[i] == 1:
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
