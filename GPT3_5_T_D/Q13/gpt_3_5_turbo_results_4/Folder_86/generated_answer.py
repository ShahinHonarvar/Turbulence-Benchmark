
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers[31:35])
    if len(sorted_nums) > 1:
        return sorted_nums[-2]
    else:
        return None
