
def if_perfect_num(nums):
    def is_perfect(num):
        if num < 1:
            return False
        
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        
        return sum(divisors) - num == num
    
    if len(nums) > 18 and is_perfect(nums[18]):
        return True
    else:
        return False
