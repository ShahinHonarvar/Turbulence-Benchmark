
def if_perfect_num(nums):
    def is_perfect(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        
        if sum(divisors) == num:
            return True
        else:
            return False
    
    if len(nums) >= 9:
        return is_perfect(nums[8])
    else:
        return False
