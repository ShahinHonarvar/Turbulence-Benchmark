
def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    
    sorted_nums = sorted(nums)
    largest_num = sorted_nums[-1]
    second_largest_num = sorted_nums[-2]
    
    if largest_num == second_largest_num:
        return None
    
    return second_largest_num
