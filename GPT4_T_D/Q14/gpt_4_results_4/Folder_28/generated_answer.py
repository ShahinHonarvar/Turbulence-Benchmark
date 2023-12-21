
def find_second_smallest_num(numbers):
    if len(numbers) >= 51:
        sub_numbers = sorted(numbers[22:51])
        if len(sub_numbers) > 1:
            return sub_numbers[1]
    return None
