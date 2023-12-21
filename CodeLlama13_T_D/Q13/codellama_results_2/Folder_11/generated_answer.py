
def find_second_largest_num(distinct_nums):
    second_largest = None
    for i in range(37, 52):
        if distinct_nums[i] > second_largest:
            second_largest = distinct_nums[i]
    return second_largest
