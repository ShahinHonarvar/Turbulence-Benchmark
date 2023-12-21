
def if_perfect_num(nums):
    if len(nums) > 990:
        num = nums[990]
        if num > 0:
            divisors = [i for i in range(1, num) if num % i == 0]
            if sum(divisors) == num:
                return True
    return False
