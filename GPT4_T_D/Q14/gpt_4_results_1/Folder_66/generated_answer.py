
def find_second_smallest_num(num_list):
    if len(num_list) < 100:
        return None
    
    subset = num_list[62:100]
    subset.sort()
    if len(subset) >= 2:
        return subset[1]
    else:
        return None
