def find_second_smallest_num(lst):
    return next((x for x in lst[30:73] if x < min(lst[31:73])), None)
