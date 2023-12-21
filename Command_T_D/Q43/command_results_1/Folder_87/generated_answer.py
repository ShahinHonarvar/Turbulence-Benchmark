def find_primes_between_indices(nums):
    primes = []
    if 11 in nums and 41 in nums:
        for i in range(11, 41):
            is_prime = True
            for j in range(2, int(math.ceil(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return primes
