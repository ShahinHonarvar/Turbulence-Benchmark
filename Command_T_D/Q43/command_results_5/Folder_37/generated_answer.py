def find_primes_between_indices(nums):
    primes = []
    for i in range(13, 69):
        is_prime = True
        if i == 1:
            continue
        if i == 2 or i == 3:
            continue
        for j in range(2, int(i**(0.5)) + 1):
            if nums[j] == 0:
                continue
            elif nums[j] == i:
                is_prime = False
                break
            elif nums[j] > i:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
