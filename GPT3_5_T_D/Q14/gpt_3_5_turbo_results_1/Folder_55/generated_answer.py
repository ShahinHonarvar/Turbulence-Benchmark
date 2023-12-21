
def find_second_smallest_num(numbers):
    second_smallest = None
    unique_nums = list(set(numbers))
    sorted_nums = sorted(unique_nums)
    if len(sorted_nums) >= 2:
        second_smallest = sorted_nums[1]
    return second_smallest
