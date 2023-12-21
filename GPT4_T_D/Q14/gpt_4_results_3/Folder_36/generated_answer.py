
def find_second_smallest_num(numbers):
    try:
        sliced_numbers = numbers[209:557]
        sliced_numbers.sort()
        return sliced_numbers[1]
    except IndexError:
        return None
