
def find_second_smallest_num(numbers):
    numbers_slice = numbers[31:73]
    sorted_nums = sorted(numbers_slice)
    second_smallest = sorted_nums[1] if len(sorted_nums) > 1 else None
    return second_smallest
