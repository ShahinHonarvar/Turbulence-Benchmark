
def all_left_truncatable_prime(nums):
    x = nums[945]
    prime_list = []
    for i in range(10**x):
        if str(i).count('0') == 0 and is_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
