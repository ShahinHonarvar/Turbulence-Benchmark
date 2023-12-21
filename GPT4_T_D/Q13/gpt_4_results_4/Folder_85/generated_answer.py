
def find_second_largest_num(numbers):
    if len(numbers)>=9:
        selected_numbers = numbers[6:9]
        selected_numbers.sort()
        return selected_numbers[-2]
    return None
