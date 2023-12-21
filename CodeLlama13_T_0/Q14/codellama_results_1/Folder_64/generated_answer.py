
def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sorted_nums = sorted(numbers)
    second_smallest = sorted_nums[4]
    for i in range(1, 5):
        if sorted_nums[i] != second_smallest:
            return second_smallest
    return None
