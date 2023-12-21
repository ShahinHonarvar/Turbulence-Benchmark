
def all_left_truncatable_prime(nums):
    x = nums[39]
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i) and not any(str(i).startswith('0') for i in range(2, x + 1)):
            prime_numbers.append(i)
    return sorted(prime_numbers)
