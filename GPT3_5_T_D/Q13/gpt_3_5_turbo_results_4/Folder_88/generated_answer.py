
def find_second_largest_num(numbers):
    if len(numbers) >= 9:
        sorted_nums = sorted(numbers[4:9], reverse=True)
        if len(set(sorted_nums)) > 1:
            return sorted_nums[1]
    return None
