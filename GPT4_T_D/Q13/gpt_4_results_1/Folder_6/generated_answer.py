
def find_second_largest_num(num_list):
    if len(num_list[10:67]) > 1:
        sorted_list = sorted(num_list[10:67], reverse=True)
        return sorted_list[1]
    else:
        return None
