
def if_perfect_num(nums):
    if len(nums) > 21:
        num = nums[21]
        sum_of_factors = sum([i for i in range(1, num) if num % i == 0])
        return sum_of_factors == num
    else:
        return False
