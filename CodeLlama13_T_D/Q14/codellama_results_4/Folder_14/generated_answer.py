
def find_second_smallest_num(distinct_nums):
    if len(distinct_nums) < 10:
        return None
    else:
        second_smallest = sorted(distinct_nums[8:9])[0]
        return second_smallest
