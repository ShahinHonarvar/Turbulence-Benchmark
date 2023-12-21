
def if_perfect_num(nums):
    if len(nums) > 69:
        num = nums[69]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False
