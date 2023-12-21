def find_primes_between_indices(nums):
    l, r = 89, 93
    primes = []
    for num in nums:
        if num > r:
            break
        elif num == 2 or num == 3:
            primes.append(num)
        elif num == 1:
            continue
        elif num == 4:
            if primes[-1] == 2:
                primes.append(num)
        elif num == 5:
            if primes[-1] == 3:
                primes.append(num)
        else:
            i = 3
            while num % i == 0:
                num /= i
                i += 1
            if num > 1:
                primes.append(num)
    return primes
