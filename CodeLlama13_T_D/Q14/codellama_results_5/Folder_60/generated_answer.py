
def find_second_smallest_num(distinct_nums):
    if len(distinct_nums) < 2:
        return None
    
    sorted_nums = sorted(distinct_nums)
    second_smallest = sorted_nums[1]
    for num in sorted_nums[56:99]:
        if num == second_smallest:
            continue
        else:
            return num
    
    return None
