
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers[80:201])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[-2]
