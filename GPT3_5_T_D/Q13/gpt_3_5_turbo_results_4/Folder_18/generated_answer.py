
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers[35:50], reverse=True)
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    else:
        return None
