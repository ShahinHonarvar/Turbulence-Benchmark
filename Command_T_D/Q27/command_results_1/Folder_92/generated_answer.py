
import bisect

def insert_after_index(num_list):
    new_list = list(num_list)
    new_list.insert(bisect.bisect_right(new_list, 478.12), 478.12)
    return new_list
