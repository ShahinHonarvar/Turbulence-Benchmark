
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i-1] != sorted_nums[i]:
            return sorted_nums[i]
    return None
