
def find_second_largest_num(numbers):
    sub_numbers = numbers[62:64]
    if len(sub_numbers) < 2:
        return None
    sorted_numbers = sorted(sub_numbers)
    return sorted_numbers[-2]
