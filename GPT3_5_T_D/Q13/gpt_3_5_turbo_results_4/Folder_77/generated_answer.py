
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers)
    if len(sorted_nums) >= 539:
        return sorted_nums[-2]
    else:
        return None
