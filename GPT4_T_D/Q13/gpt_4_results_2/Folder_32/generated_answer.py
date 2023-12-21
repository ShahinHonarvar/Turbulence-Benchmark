
def find_second_largest_num(numbers):
    try:
        selected_numbers = numbers[21:98]
        selected_numbers.sort()
        return selected_numbers[-2]
    except IndexError:
        return None
