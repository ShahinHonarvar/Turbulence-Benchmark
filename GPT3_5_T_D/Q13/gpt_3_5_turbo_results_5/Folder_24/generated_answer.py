
def find_second_largest_num(lst):
    lst_74_to_95 = lst[74:96]
    if len(lst_74_to_95) >= 2:
        lst_74_to_95.sort()
        return lst_74_to_95[-2]
    else:
        return None
