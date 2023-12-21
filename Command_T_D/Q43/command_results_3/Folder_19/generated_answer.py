def find_primes_between_indices(nums):
    primes = []
    for num in nums[21:97]:
        is_prime = True
        if num < 2:
            continue
        if num == 2 or num == 3:
            continue
        for i in range(2, int(num**(0.5)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)
