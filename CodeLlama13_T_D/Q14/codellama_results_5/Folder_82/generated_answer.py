
def find_second_smallest_num(distinct_nums):
    sorted_nums = sorted(distinct_nums)
    for i in range(20, 201):
        if sorted_nums[i] == sorted_nums[i-1]:
            continue
        else:
            return sorted_nums[i-1]
    return None
