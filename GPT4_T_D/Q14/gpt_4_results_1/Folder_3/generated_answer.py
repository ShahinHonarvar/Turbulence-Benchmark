
def find_second_smallest_num(numbers):
    if len(numbers) >= 55:
        selected_nums = sorted(numbers[27:56])
        if len(selected_nums) > 1:
            return selected_nums[1]
    return None
