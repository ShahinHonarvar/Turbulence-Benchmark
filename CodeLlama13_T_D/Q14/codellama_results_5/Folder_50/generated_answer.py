
def find_second_smallest_num(nums):
    smallest = None
    second_smallest = None
    for i in range(42, 69):
        num = nums[i]
        if smallest is None or num < smallest:
            smallest = num
            continue
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest
