
def find_second_largest_num(num_list):
    if len(num_list[25:88]) < 2:
        return None
    else:
        return sorted(num_list[25:88], reverse=True)[1]
