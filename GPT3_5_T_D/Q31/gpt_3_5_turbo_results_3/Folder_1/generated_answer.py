
def if_perfect_num(nums):
    def is_perfect(num):
        divisors = [1]
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num // i)
        return sum(divisors) == num
    
    if len(nums) > 85 and is_perfect(nums[85]):
        return True
    else:
        return False
