
def find_second_largest_num(distinct_list):
    if len(distinct_list) < 2:
        return None
    
    sorted_list = sorted(distinct_list, reverse=True)
    for i in range(26, 53):
        if sorted_list[i] != sorted_list[i-1]:
            return sorted_list[i]
    
    return None
