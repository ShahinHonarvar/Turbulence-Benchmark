
def find_second_largest_num(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) > 1:
        return unique_numbers[1]
    else:
        return None
