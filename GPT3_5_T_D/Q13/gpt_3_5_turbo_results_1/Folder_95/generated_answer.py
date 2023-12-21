
def find_second_largest_num(numbers):
    sub_list = numbers[82:87]
    sub_list.sort()
    return sub_list[-2] if len(sub_list) >= 2 else None
