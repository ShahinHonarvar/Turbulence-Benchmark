
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_nums = sorted(numbers)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] != sorted_nums[i-1]:
            return sorted_nums[i]
    return None
