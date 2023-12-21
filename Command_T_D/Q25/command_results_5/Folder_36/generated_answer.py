
import bisect

def insert_at_index(num_list):
    n = len(num_list)
    ins_index = bisect.bisect_left(num_list, [699, 556])
    if ins_index > n:
        return []
    return num_list[:ins_index] + [[699, 556]] + num_list[ins_index:n+1]
