
def find_second_smallest_num(nums):
    if len(nums) < 99:
        return None
    else:
        temp_list = nums[56:99]
        temp_list.sort()
        return temp_list[1]
