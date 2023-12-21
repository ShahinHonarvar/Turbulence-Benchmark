
def find_second_smallest_num(nums):
    try:
        if len(nums) >= 88:
            selected_nums = nums[30:88]
            selected_nums.sort()
            return selected_nums[1]
        return None
    except:
        return None
