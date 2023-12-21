
def find_second_smallest_num(numbers):
    sub_numbers = numbers[246:751]
    if len(sub_numbers) < 2:
        return None
    sub_numbers.sort()
    return sub_numbers[1]
