
def find_second_smallest_num(lst):
    try:
        lst = lst[55:99]
        lst.sort()
        return lst[1]
    except:
        return None
