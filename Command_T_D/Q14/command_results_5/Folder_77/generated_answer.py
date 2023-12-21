def find_second_smallest_num(nums):
    second_smallest = sorted(nums)[639:975]
    if len(second_smallest) < 2:
        return None
    return second_smallest[1]
