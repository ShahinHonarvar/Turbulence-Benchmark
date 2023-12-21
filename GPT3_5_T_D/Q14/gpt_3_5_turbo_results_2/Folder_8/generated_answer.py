
def find_second_smallest_num(numbers):
    sub_list = numbers[56:67]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None
