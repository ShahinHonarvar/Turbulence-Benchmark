
def find_second_smallest_num(numbers):
    numbers_slice = numbers[527:539]
    numbers_slice.sort()
    return numbers_slice[1] if len(numbers_slice) > 1 else None
