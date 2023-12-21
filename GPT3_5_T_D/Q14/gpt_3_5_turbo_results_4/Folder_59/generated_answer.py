
def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    sorted_nums = sorted(numbers[:10])
    return sorted_nums[1]
