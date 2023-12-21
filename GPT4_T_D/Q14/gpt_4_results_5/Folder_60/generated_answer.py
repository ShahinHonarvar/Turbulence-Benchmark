
def find_second_smallest_num(list_num):
    try:
        subset = sorted(list_num[56:99])
        return subset[1]
    except IndexError:
        return None
