
def find_second_smallest_num(numbers):
    if len(numbers)<606:
        return None
    sorted_nums = sorted(numbers[533:606])
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]
