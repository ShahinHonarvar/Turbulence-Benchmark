
def all_pos_ints_exclusive(nums_list):
    pos_nums = [num for num in nums_list[1:-1] if num > 0]
    return pos_nums
