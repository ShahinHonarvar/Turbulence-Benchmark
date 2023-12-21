
def find_second_largest_num(numbers):
    if len(numbers) < 41:
        return None
    else:
        sliced_list = numbers[28:41]
        sliced_list.sort()
        return sliced_list[-2] if len(sliced_list) > 1 else None
