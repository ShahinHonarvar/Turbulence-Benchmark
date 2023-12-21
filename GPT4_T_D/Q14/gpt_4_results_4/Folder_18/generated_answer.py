
def find_second_smallest_num(num_list):
    if len(num_list) < 49:
        return None
    else:
        subsection = sorted(num_list[30:49])
        if len(subsection) < 2:
            return None
        else:
            return subsection[1]
