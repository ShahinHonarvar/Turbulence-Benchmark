
def find_second_smallest_num(numbers):
    numbers_slice = numbers[62:79]
    if len(numbers_slice) < 2:
        return None
    else:
        numbers_slice.sort()
        return numbers_slice[1]
