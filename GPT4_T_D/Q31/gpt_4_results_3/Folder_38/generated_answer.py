
def if_perfect_num(nums):
    if len(nums) > 38:
        num = nums[38]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False
