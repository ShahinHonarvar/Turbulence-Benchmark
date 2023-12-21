
def if_perfect_num(nums):
    num = nums[15]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num * 2
