
def find_second_largest_num(lst):
    try:
        lst = sorted(lst[:9])
        return lst[-2]
    except IndexError:
        return None
