
def if_perfect_num(nums):
    index_4 = nums[4]
    divisor_sum = sum([i for i in range(1,index_4) if index_4%i == 0])
    return divisor_sum == index_4
