
import bisect

def insert_at_index(my_list):
    result_list = list(my_list)
    result_list.insert(bisect.bisect_left(result_list, [28, 53]), [28, 53])
    return result_list
