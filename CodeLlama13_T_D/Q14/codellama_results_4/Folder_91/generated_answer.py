
def find_second_smallest_num(numbers):
    if len(numbers) <= 5:
        return None
    else:
        sorted_nums = sorted(numbers[0:6])
        second_smallest = sorted_nums[1]
        return second_smallest
