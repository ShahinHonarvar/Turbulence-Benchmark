def all_left_truncatable_prime(nums):
    x = int(nums[98])
    primes = []
    for num in range(2, x // 2):
        if num == 2 or num == 3:
            primes.append(num)
        elif num in nums:
            continue
        elif num == 1:
            break
        elif all(nums[num:num + i] == 'prime' for i in range(1, len(num) + 1)):
            primes.append(num)
    return sorted(set(primes))
