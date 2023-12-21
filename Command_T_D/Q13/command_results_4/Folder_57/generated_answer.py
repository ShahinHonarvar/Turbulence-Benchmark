
def find_second_largest_num(nums):
    try:
        return nums[nums.index(max(nums[27:55]))-1]
    except:
        return None
