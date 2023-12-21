
def all_right_truncatable_prime(nums):
    x = nums[97]
    prime_list = []
    for i in range(10, x):
        if is_prime(i) and is_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
