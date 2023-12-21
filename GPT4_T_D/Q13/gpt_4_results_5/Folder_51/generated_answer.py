
def find_second_largest_num(numbers):
    try:
        sorted_nums = sorted(numbers[1:9], reverse=True)
        return sorted_nums[1] if len(sorted_nums) > 1 else None
    except IndexError:
        return None
