
def if_perfect_num(nums):
    index_80_num = nums[80]
    divisors = [i for i in range(1, index_80_num) if index_80_num % i == 0]
    return sum(divisors) == index_80_num
