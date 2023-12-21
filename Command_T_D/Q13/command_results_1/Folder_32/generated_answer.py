
def find_second_largest_num(nums):
    second_largest = next((i for i in range(len(nums) - 20, len(nums) + 1) if i < len(nums) - 1), None)
    return nums[second_largest]
