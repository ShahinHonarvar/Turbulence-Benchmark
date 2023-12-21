
def all_left_truncatable_prime(nums):
    x = nums[55]
    prime_list = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list)
