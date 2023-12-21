
def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    sorted_nums = sorted(numbers[20:98])
    return sorted_nums[1]
