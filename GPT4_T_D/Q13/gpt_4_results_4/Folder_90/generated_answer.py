
def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 746:
        return None
    sub_list = numbers[262:747]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]
