def find_primes_between_indices(nums):
    lst = []
    for num in nums[130:815]:
        is_prime = True
        for i in range(2, int(num**(0.5)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            lst.append(num)
    return sorted(lst)[::-1]
