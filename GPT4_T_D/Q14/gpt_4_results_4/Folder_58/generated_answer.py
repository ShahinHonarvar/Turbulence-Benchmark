
def find_second_smallest_num(nums):
    new_list = nums[310:371]
    if len(new_list) < 2:
        return None
    else:
        new_list.sort()
        return new_list[1]
