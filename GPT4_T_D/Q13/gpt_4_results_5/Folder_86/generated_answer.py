
def find_second_largest_num(num_list):
    try:
        subset_list = num_list[31:35]
        subset_list.sort(reverse=True)
        if len(subset_list) > 1:
            return subset_list[1]
        else:
            return None
    except:
        return None
