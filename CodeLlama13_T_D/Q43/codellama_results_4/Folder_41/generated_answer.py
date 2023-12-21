
def find_primes_between_indices(numbers):
    prime_nums = []
    for i in range(45, 81):
        if is_prime(numbers[i]):
            prime_nums.append(numbers[i])
    return sorted(prime_nums, reverse=True)
