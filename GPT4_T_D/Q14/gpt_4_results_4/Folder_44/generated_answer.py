
def find_second_smallest_num(lst):
    try:
        return sorted(lst[91:100])[1]
    except IndexError:
        return None
