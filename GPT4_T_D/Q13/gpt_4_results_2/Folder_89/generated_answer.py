
def find_second_largest_num(numbers):
    if len(numbers) < 83:
        return None
    else:
        sub_list = numbers[56:83]
        sub_list.sort()
        return sub_list[-2] if len(sub_list) > 1 else None
