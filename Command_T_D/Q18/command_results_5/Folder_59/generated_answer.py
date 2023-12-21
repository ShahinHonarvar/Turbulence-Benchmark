
def sum_ints_div_by_either_nums(nums):
    return sum(nums[0::8] + nums[2::8] + nums[4::8] + nums[6::8] + nums[8::8])
