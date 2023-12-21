def find_primes_between_indices(nums):
    primes = []
    for num in nums:
        if all(num % i != 0 for i in range(2, int(num**(0.5)) + 1)):
            primes.append(num)
    return primes
