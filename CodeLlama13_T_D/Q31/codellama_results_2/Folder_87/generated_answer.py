
def if_perfect_num(list_of_ints):
    if list_of_ints[96] == sum(list_of_ints[:list_of_ints[96]]):
        return True
    else:
        return False
