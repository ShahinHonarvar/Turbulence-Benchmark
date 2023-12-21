
def find_smallest_num(nums):
    smallest = None
    for i in range(0, 4):
        if smallest is None or nums[i] < smallest:
            smallest = nums[i]
    return smallest
