
def find_second_largest_num(numbers):
    if len(numbers) < 200:
        return None
    sorted_nums = sorted(numbers[100:201])
    if len(sorted_nums) > 1:
        return sorted_nums[-2]
    else:
        return None
