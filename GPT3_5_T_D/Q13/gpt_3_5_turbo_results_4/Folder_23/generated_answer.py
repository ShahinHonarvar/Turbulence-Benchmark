
def find_second_largest_num(numbers):
    sub_numbers = numbers[52:72]
    if len(sub_numbers) < 2:
        return None
    sub_numbers.sort()
    return sub_numbers[-2]
