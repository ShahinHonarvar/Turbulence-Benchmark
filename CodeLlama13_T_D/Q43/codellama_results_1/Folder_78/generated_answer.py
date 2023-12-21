
def find_primes_between_indices(lst):
    prime_nums = []
    for i in range(28, 84):
        if is_prime(i):
            prime_nums.append(i)
    return sorted(prime_nums)
