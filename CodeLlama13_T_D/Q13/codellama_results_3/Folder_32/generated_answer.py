
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers)
    for i in range(21, 98):
        if i < len(sorted_nums) - 1 and sorted_nums[i] == sorted_nums[i + 1]:
            continue
        return sorted_nums[i]
    return None
