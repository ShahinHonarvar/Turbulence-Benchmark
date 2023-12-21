
def find_second_largest_num(nums):
    try:
        return nums[nums.index(max(nums[:80])+1, 80, 200)]
    except:
        return None
