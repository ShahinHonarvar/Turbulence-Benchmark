
def find_second_largest_num(lst):
    segment = lst[26:53]
    if len(segment) < 2:
        return None
    else:
        segment.sort()
        return segment[-2]
