
def find_second_largest_num(numbers):
    nums_section = numbers[36:47]
    if len(nums_section) < 2:
        return None
    nums_section.sort()
    return nums_section[-2]
