
def all_right_truncatable_prime(nums):
    x = nums[49]
    prime_list = []
    for i in range(10, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)
