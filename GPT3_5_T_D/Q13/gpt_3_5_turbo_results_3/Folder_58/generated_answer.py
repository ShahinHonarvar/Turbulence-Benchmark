
def find_second_largest_num(numbers):
    sub_list = numbers[209:557]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1]
