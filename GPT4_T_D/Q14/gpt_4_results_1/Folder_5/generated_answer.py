
def find_second_smallest_num(lst):
    try:
        sub_list = sorted(lst[3:6])
        return sub_list[1]
    except IndexError:
        return None
