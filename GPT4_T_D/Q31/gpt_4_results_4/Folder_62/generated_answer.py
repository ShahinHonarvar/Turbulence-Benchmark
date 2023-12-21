
def if_perfect_num(nums):
    if len(nums) < 927:
        return False

    num = nums[926]
    divisors = [i for i in range(1, num) if num % i == 0]

    return sum(divisors) == num
