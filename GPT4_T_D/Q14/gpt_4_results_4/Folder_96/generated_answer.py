
def find_second_smallest_num(numbers):
    if len(numbers)<200:
        return None
    nums_slice = numbers[50:201]
    nums_slice.sort()
    return nums_slice[1] if len(nums_slice)>1 else None
