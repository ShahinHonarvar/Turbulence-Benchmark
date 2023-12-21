
def if_perfect_num(nums):
    if len(nums) > 33:
        num = nums[33]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
