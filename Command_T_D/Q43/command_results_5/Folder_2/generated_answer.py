def find_primes_between_indices(nums):
    primes = []
    for index in range(167, 785):
        if nums[index] % 2 == 0 or nums[index] == 1:
            continue
        else:
            for multiple in range(3, int(nums[index**0.5]) + 1):
                if nums[index] % multiple == 0:
                    break
                else:
                    primes.append(nums[index])
    return sorted(primes)
