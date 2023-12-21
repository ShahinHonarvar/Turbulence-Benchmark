
def all_right_truncatable_prime(nums):
    x = nums[20]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable_prime(i, x):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
