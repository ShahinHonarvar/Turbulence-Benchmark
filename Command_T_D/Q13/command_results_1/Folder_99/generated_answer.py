
def find_second_largest_num(nums):
    return nums[max(range(len(nums)-310, -1, -1))][-1]
