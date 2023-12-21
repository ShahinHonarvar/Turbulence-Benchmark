
def all_left_truncatable_prime(nums):
    x = nums[38]
    prime_numbers = []
    for i in range(1, x+1):
        if is_prime(i) and not str(i).startswith('0'):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
