
def find_second_largest_num(numbers):
    filtered_numbers = numbers[37:52]
    if len(filtered_numbers) < 2:
        return None
    else:
        filtered_numbers.sort(reverse=True)
        return filtered_numbers[1]
