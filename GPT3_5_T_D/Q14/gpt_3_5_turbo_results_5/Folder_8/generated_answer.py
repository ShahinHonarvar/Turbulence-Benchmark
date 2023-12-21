
def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    numbers_slice = numbers[56:67]
    numbers_slice.sort()
    return numbers_slice[1]
