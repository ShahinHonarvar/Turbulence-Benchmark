
def find_second_smallest_num(numbers):
    numbers_partial = numbers[80:201]
    if len(numbers_partial) < 2:
        return None
    else:
        numbers_partial.sort()
        return numbers_partial[1]
