
def find_second_largest_num(num_list):
    if len(num_list) < 63:
        return None
    else:
        num_list_subset = sorted(num_list[62:100], reverse=True)
        if len(num_list_subset) < 2:
            return None
        else:
            return num_list_subset[1]
