
def find_second_smallest_num(lst):
    try:
        segment = lst[50:55]
        segment.sort()
        return segment[1]
    except:
        return None
