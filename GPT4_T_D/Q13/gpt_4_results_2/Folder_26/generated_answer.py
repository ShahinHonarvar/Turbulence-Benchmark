
def find_second_largest_num(numbers):
    if len(numbers[62:100]) < 2:
        return None

    sorted_nums = sorted(numbers[62:100], reverse=True)
    return sorted_nums[1]
