
def find_second_largest_num(lst):
    try:
        sliced_list = lst[12:93]
        if len(sliced_list)<2:
            return None
        else:
            sliced_list.sort()
            return sliced_list[-2]
    except:
        return None
