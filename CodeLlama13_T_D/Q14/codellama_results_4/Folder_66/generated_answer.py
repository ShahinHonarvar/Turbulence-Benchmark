
def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = None
    for i in range(62, 100):
        if sorted_nums[i] != sorted_nums[i-1]:
            second_smallest = sorted_nums[i]
            break
    return second_smallest
