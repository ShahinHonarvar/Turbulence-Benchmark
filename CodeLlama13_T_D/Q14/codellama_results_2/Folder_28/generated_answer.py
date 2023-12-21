
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    for i in range(22, 51):
        if i < len(sorted_nums) - 1 and sorted_nums[i] == sorted_nums[i + 1]:
            return None
    return sorted_nums[22]
