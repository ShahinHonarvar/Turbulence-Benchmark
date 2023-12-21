
def all_left_truncatable_prime(nums):
    x = nums[19]
    prime_list = []
    for i in range(2, x):
        if is_prime(i) and not contains_zero(str(i)):
            prime_list.append(i)
    return sorted(prime_list)
