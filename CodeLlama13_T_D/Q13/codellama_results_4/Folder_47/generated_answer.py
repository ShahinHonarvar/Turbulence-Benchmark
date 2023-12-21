
def find_second_largest_num(distinct_nums):
    if len(distinct_nums) <= 36:
        return None
    
    sorted_nums = sorted(distinct_nums)[37:77]
    second_largest = sorted_nums[1]
    return second_largest
