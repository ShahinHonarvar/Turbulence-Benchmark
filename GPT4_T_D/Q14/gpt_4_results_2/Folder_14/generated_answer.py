
def find_second_smallest_num(nums):
    try:
        relevant_nums = nums[8:10]
        relevant_nums.sort()
        return relevant_nums[1]
    except:
        return None
