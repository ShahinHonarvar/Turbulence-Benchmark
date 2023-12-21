def find_primes_between_indices(nums):
    l, r = nums[38], nums[55]
    if l < 2:
        return []
    if l == 2 or l == 3:
        return [l, l + 1]
    primes = []
    for num in range(l, r + 1):
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
    return primes
