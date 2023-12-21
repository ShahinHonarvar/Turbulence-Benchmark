
def find_second_smallest_num(numbers):
    if len(numbers)<70:
        return None
    else:
        sub_list = numbers[70:85]
        sub_list.sort()
        if len(sub_list)>=2:
            return sub_list[1]
        else:
            return None
