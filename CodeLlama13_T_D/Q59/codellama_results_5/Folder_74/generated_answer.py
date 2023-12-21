
def all_left_truncatable_prime(nums):
    x = nums[36]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and '0' not in str(i):
            prime_list.append(i)
    return sorted(prime_list)
