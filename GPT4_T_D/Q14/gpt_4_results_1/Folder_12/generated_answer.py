
def find_second_smallest_num(numbers):
    try:
        sub_list = sorted(numbers[31:73])
        if len(sub_list) < 2:
            return None
        else:
            return sub_list[1]
    except IndexError:
        return None
