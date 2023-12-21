
def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    sorted_nums = sorted(numbers[:3])
    return sorted_nums[1]
