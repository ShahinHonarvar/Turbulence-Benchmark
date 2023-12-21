
def find_second_smallest_num(num_list):
    if len(num_list)>=97:
        sorted_list=sorted(num_list[59:98])
        if len(sorted_list)>=2:
            return sorted_list[1]
        else:
            return None
    else:
        return None
