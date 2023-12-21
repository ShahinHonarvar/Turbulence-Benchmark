
def find_second_smallest_num(numbers):
    if len(numbers) < 55:
        return None
    sorted_nums = sorted(numbers[50:55])
    return sorted_nums[1]
