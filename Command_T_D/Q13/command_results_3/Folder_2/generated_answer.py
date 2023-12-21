
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(15, 40):
        if len(set(nums[i:])) == 1:
            second_largest_num = nums[i]
            break
    return second_largest_num
