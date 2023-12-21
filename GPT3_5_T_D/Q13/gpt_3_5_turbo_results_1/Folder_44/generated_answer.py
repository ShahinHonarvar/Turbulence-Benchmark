
def find_second_largest_num(numbers):
    sub_list = numbers[13:69]
    sub_list.sort(reverse=True)
    if len(sub_list) >= 2:
        return sub_list[1]
    else:
        return None
