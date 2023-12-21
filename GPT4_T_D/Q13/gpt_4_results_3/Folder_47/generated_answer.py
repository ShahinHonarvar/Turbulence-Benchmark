
def find_second_largest_num(numbers):
    try:
        numbers = numbers[37:77]
        numbers.sort()
        return numbers[-2]
    except IndexError:
        return None
