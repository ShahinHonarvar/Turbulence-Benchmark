
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None

    sorted_nums = sorted(numbers)
    second_smallest = sorted_nums[1]

    for i in range(2, len(sorted_nums)):
        if sorted_nums[i] == second_smallest:
            continue
        else:
            return None

    return second_smallest
