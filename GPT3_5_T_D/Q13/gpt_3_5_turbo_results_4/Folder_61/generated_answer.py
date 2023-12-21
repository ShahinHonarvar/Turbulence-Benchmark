
def find_second_largest_num(numbers):
    sorted_nums = sorted(set(numbers))
    if len(sorted_nums) >= 2:
        return sorted_nums[-2]
    else:
        return None
