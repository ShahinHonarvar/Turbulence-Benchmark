
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers[:9])
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[-2]
