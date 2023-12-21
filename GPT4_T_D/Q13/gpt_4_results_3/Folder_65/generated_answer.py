
def find_second_largest_num(numbers):
    sub_list = numbers[56:99]
    if len(sub_list) > 1:
        sub_list.sort(reverse=True)
        return sub_list[1]
    else:
        return None
