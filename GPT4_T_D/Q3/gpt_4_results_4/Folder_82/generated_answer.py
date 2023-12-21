
def all_pos_ints_inclusive(lst):
    start = 20 if len(lst) > 20 else len(lst)
    end = 200 if len(lst) > 200 else len(lst)

    return [number for number in lst[start:end+1] if number > 0]
