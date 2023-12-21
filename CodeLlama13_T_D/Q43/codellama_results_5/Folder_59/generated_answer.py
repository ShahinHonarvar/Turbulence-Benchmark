
def find_primes_between_indices(nums):
    primes = []
    for i in range(5, 9):
        if nums[i] > 1:
            for j in range(2, int(nums[i]**0.5) + 1):
                if nums[i] % j == 0:
                    break
            else:
                primes.append(nums[i])
    return sorted(primes, reverse=True)
