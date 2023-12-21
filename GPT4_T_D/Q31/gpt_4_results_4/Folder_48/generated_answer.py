
def if_perfect_num(nums):
    if len(nums) <= 247:
        return False
    num = nums[247]
    divisors = [i for i in range(1,num) if num%i == 0]
    return sum(divisors) == num
