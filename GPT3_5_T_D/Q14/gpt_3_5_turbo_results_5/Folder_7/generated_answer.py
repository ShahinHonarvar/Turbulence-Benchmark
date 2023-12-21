
def find_second_smallest_num(numbers):
    sublist = numbers[686:988]
    unique_nums = list(set(sublist))
    if len(unique_nums) <= 1:
        return None
    else:
        unique_nums.sort()
        return unique_nums[1]
