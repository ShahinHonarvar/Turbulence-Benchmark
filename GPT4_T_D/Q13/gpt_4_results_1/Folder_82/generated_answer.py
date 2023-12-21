
def find_second_largest_num(nums):
    if len(nums) < 21:
        return None
    relevant_nums = nums[20:201] 
    if len(relevant_nums) < 2:
        return None
    relevant_nums.sort()
    return relevant_nums[-2]
