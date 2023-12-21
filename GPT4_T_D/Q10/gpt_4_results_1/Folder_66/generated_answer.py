
def all_odd_ints_exclusive(lst):
    lst = lst[14:76] # get elements between index 13 and 76 exclusively
    result = [num for num in lst if num % 2 != 0] # filter odd integers
    return result
