
def find_second_largest_num(distinct_nums):
    if len(distinct_nums) < 3:
        return None
    second_largest = None
    for i in range(34, 56):
        current = distinct_nums[i]
        if second_largest is None or current > second_largest:
            second_largest = current
    return second_largest
