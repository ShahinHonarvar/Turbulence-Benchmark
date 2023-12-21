
def find_second_smallest_num(numbers):
    nums = numbers[29:94]
    unique_nums = list(set(nums))
    sorted_nums = sorted(unique_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
