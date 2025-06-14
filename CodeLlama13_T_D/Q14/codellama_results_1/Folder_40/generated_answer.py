
def find_second_smallest_num(distinct_nums):
    if len(distinct_nums) < 3:
        return None
    second_smallest = distinct_nums[1]
    for i in range(2, len(distinct_nums)):
        if distinct_nums[i] < second_smallest:
            second_smallest = distinct_nums[i]
    return second_smallest
