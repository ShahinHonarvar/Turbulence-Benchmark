
def find_largest_num(lst):
    if len(lst) > 111:
        return max(lst[111:112])
    else:
        return "List is not long enough"
