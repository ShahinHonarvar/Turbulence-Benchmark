def find_second_smallest_num(lst):
    return next((v for v in lst if v < lst[0]), None)
