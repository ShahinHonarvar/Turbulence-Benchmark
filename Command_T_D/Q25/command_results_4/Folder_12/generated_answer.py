
import bisect

def insert_at_index(num_list):
    return [x for x in num_list] + [96] + [x for x in num_list[bisect.bisect_left(num_list, 96)]]
