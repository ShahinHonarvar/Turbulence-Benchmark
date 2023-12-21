
def find_second_largest_num(nums):
    second_largest = max(nums[100:200], key=lambda x: nums.count(x))
    return second_largest if second_largest in nums else None
