
def find_second_largest_num(numbers):
    sub_numbers = numbers[5:8]
    if len(sub_numbers) < 2:
        return None
    largest = max(sub_numbers)
    sub_numbers.remove(largest)
    return max(sub_numbers)
