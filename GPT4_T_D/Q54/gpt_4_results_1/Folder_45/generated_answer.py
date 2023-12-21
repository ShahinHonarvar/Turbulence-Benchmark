
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[61]
    rtp_list = []
    
    def is_right_truncatable(num):
        num_str = str(num)
        return all(isprime(int(num_str[:i])) for i in range(len(num_str), 0, -1))

    for i in range(2, x):
        if is_right_truncatable(i):
            rtp_list.append(i)

    return sorted(rtp_list)
