
def all_left_truncatable_prime(nums):
    x = nums[11]
    prime_list = []
    
    for i in range(2, x+1):
        if is_prime(i) and not contains_0(str(i)):
            prime_list.append(i)
            
    return sorted(prime_list)
