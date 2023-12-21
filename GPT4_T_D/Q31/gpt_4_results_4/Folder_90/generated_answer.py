
def if_perfect_num(nums):
    if len(nums) > 263:
        num = nums[263]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
