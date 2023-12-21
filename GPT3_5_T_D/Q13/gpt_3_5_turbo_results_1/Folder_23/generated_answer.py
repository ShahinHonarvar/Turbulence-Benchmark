
def find_second_largest_num(nums):
    if len(nums) < 72:
        return 'None'
    nums.sort()
    return nums[-2]
