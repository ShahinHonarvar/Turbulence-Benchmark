
def find_second_largest_num(numbers):
    if len(numbers) < 200:
        return None
    if len(numbers) == 200:
        return numbers[-1]
    else:
        selected_numbers = numbers[200:201]
        if len(selected_numbers) < 2:
            return None
        else:
            selected_numbers.sort()
            return selected_numbers[-2]
