
def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    else:
        portion = lst[8:10]
        portion.sort()
        return portion[-2]
