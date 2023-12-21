def find_primes_between_indices(nums):
    result = []
    for num in nums[11:]:
        is_prime = True
        if num < 2:
            continue
        elif num == 2 or num == 3:
            pass
        elif num % 2 == 0 or num % 3 == 0:
            is_prime = False
            break
        for i in range(5, int(num**(0.5)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
    return result
