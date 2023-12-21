
def find_primes_between_indices(nums):
    primes = []
    nums = nums[66:80]
    for num in nums:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)
