
import bisect

def insert_at_index(my_list):
    insert_idx = bisect.bisect_left(my_list, 304.62)
    my_list.insert(insert_idx, 304.62)
    return my_list
