
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers[22:64])
    if len(sorted_nums) >= 2:
        return sorted_nums[-2]
    return None
