
def find_second_smallest_num(lst):
    sublist = lst[30:88]
    try:
        sublist.remove(min(sublist))
        return min(sublist)
    except ValueError:
        return None
