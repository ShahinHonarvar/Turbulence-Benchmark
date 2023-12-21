
def find_second_largest_num(numb_list):
    sublist = numb_list[15: 40] 
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[-2]
