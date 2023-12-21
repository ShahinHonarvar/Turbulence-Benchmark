
def find_second_largest_num(numbers):
    sub_list = numbers[28:41]
    sub_list.sort(reverse=True)
    return sub_list[1] if len(sub_list) >= 2 else None
