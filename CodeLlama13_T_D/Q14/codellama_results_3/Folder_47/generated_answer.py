
def find_second_smallest_num(distinct_nums):
    second_smallest = None
    for i in range(22, 64):
        if distinct_nums[i] < second_smallest:
            second_smallest = distinct_nums[i]
    return second_smallest
