
def find_second_smallest_num(distinct_nums):
    second_smallest = None
    for i in range(1, 6):
        if distinct_nums[i] < distinct_nums[0]:
            second_smallest = distinct_nums[i]
            break
    return second_smallest
