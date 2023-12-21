
def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    else:
        selected_numbers = numbers[56:58]
        selected_numbers.sort(reverse = True)
        return selected_numbers[1]
