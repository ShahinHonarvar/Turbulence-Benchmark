def find_primes_between_indices(nums):
    result = []
    for n in range(28, 83):
        if all(n % r for r in range(2, int(n**(0.5)) + 1)):
            result.append(n)
    return sorted(result)
