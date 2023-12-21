
def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sorted_nums = sorted(numbers[1:6])
    for i in range(len(sorted_nums)):
        if sorted_nums[i] != sorted_nums[i-1]:
            return sorted_nums[i]
    return None
