
import bisect

def insert_after_index(num_list):
    idx = bisect.bisect_left(num_list, 709.87)
    return num_list[:idx] + [709.87] + num_list[idx+1:]
