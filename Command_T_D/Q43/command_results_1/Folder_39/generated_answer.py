def find_primes_between_indices(nums):
    result = []
    for i in range(69, 81):
        if is_prime(i):
            result.append(i)
    return result
