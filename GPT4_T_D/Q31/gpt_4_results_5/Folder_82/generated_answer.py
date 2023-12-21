
def if_perfect_num(nums):
    index_83_num = nums[83]
    divisors = [i for i in range(1, index_83_num) if index_83_num % i == 0]
    return sum(divisors) == index_83_num
