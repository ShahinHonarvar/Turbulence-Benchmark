
def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    sorted_nums = sorted(numbers[:4])
    return sorted_nums[1]
