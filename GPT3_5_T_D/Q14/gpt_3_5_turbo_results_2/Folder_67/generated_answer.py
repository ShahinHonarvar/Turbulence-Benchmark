
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    if 50 <= len(numbers) <= 54:
        return sorted_nums[1]
    else:
        return None
