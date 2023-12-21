
def find_second_smallest_num(numbers):
    if len(numbers[20:201]) < 2:
        return None
    else:
        sorted_nums = sorted(numbers[20:201])
        return sorted_nums[1]
