def find_primes_between_indices(nums):
    primes = []
    for num in nums:
        if num <= 1:
            continue
        elif num <= 3:
            break
        elif num % 2 == 0 or num % 3 == 0:
            continue
        else:
            for i in range(5, int(num ** .5) + 1):
                if num % i == 0:
                    break
                elif i * i > num:
                    break
            else:
                primes.append(num)
    return sorted(primes)[::-1]
