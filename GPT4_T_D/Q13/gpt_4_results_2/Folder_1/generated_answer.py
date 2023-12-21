
def find_second_largest_num(numbers):
    numbers_slice = numbers[31:73]
    if len(numbers_slice) < 2:
        return None
    numbers_slice.sort()
    return numbers_slice[-2]
