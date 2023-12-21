
def find_primes_between_indices(int_list):
    prime_numbers = [i for i in int_list[46:62] if i > 1 and all(i%j != 0 for j in range(2, int(i ** 0.5) + 1))]
    return sorted(prime_numbers)
