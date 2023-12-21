
def gcf_two_nums(lst):
    index_18 = lst[18]
    index_37 = lst[37]
    
    while index_37 != 0:
        index_18, index_37 = index_37, index_18 % index_37
    
    return index_18
