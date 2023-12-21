def find_primes_between_indices(nums):
    start, stop = 45, 80
    primes = []
    for num in nums:
        if num == start:
            continue
        if num == stop:
            break
        if all(num % i != 0 for i in range(2, int(num ** .5) + 1)):
            primes.append(num)
    return sorted(set(primes))
