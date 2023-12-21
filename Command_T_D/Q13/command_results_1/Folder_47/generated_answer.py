
def find_second_largest_num(lst):
    res = next((y for y in lst[37:-1] + lst[38:76] if y > lst[-1]), None)
    return res
