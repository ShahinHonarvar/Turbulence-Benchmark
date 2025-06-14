
def all_left_truncatable_prime(nums):
    x = nums[79]
    prime_list = []
    for i in range(10**8, x+1):
        if is_prime(i) and not '0' in str(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
