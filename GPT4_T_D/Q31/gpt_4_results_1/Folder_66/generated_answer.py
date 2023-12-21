
def if_perfect_num(nums):
    if len(nums) <= 42:
        return False
    else:
        num = nums[42]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
