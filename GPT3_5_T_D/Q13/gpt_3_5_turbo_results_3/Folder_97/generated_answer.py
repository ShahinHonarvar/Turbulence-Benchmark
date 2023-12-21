
def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers[40:81])
    return None if len(sorted_numbers) < 2 else sorted_numbers[-2]
