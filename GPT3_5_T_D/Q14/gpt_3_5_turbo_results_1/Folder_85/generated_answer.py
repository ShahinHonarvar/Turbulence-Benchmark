
def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sorted_nums = sorted(numbers[:7])
    return sorted_nums[1]
