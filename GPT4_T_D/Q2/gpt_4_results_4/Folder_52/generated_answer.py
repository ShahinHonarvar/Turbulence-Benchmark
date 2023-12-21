
def all_ints_exclusive(lst):
    if type(lst) == list and all(isinstance(i, int) for i in lst):
        return lst[70:97]
