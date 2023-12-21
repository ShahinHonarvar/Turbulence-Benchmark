def find_primes_between_indices(nums):
    primes = []
    for num in nums[19:71]:
        if all(num % d for d in range(2, int(num**(0.5)) + 1)):
            primes.append(num)
    return sorted(primes)
