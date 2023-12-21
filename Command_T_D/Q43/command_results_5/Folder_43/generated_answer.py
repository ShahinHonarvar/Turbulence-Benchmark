def find_primes_between_indices(nums):
    primes = []
    for num in nums:
        if num > 2:
            for i in range(3, int(num**(0.5)) + 1):
                if num % i == 0:
                    break
                elif i * i > num:
                    primes.append(num)
                    break
    return primes
