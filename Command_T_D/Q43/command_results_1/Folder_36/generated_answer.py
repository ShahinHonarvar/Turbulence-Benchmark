def find_primes_between_indices(nums):
    primes = []
    for num in nums[229:850]:
        if all(num % i != 0 for i in range(3, int(num**(0.5)) + 1)):
            primes.append(num)
    return sorted(primes)
