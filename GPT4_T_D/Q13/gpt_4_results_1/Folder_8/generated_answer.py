
def find_second_largest_num(numbers):
    if len(numbers) > 23:
        try:
            second_largest = sorted(numbers[23:24])[-2]
        except IndexError:
            return None
        return second_largest
    else:
        return None
