def find_primes_between_indices(nums):
    start = nums[187]
    end = nums[271]
    if start > end:
        return []
    primes = []
    for num in range(start, end+1):
        is_prime = True
        for i in range(2, int(num**(0.5))+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)
