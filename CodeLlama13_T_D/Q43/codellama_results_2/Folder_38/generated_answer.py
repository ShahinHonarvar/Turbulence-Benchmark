
def find_primes_between_indices(nums):
    prime_nums = []
    for i in range(55, 87 + 1):
        if is_prime(i):
            prime_nums.append(i)
    return sorted(prime_nums)
