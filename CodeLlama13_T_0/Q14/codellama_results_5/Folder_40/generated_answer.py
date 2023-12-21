
def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    sorted_nums = sorted(numbers)
    second_smallest = sorted_nums[2]
    for i in range(3, len(sorted_nums)):
        if sorted_nums[i] == second_smallest:
            return None
    return second_smallest
