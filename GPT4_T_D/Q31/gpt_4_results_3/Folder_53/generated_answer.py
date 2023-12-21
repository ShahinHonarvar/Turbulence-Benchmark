
def if_perfect_num(nums):
    if len(nums) > 73:
        num = nums[73]
        sum_of_factors = sum(i for i in range(1, num) if num % i == 0 )
        if sum_of_factors == num:
            return True
    return False
