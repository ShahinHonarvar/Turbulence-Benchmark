
def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    sorted_nums = sorted(numbers[30:49])
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] != sorted_nums[i-1]:
            return sorted_nums[i-1]
    return None
