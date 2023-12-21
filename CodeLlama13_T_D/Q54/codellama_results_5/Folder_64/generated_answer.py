
def all_right_truncatable_prime(nums):
    x = nums[4]
    prime_list = []
    
    for i in range(2, x+1):
        if is_prime(i):
            prime_list.append(i)
        
    right_truncatable_prime_list = []
    
    for i in prime_list:
        for j in range(len(str(i))-1, 0, -1):
            if is_prime(int(str(i)[0:j])):
                right_truncatable_prime_list.append(int(str(i)[0:j]))
    
    return sorted(right_truncatable_prime_list)
