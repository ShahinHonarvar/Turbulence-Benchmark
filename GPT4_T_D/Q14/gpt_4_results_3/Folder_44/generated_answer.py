
def find_second_smallest_num(lst):
    if len(lst[91:100]) < 2:
        return None
    else:
        return sorted(lst[91:100])[1]
