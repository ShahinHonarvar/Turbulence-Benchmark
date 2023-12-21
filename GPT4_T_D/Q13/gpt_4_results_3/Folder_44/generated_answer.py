
def find_second_largest_num(numbers):
    try:
        if len(numbers) >= 69:
            sliced_numbers = numbers[13:69]
            sliced_numbers.sort()
            return sliced_numbers[-2]
        else:
            return None
    except IndexError:
        return None
