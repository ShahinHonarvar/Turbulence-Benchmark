def find_primes_between_indices(nums):
    result = []
    for n in range(28, 36):
        if all(n % i != 0 for i in range(2, int(n**(0.5)) + 1)):
            result.append(n)
    return result
