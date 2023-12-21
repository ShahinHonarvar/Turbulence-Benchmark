
def find_second_smallest_num(num_list):
    if len(num_list[82:87]) >= 2:
        num_list_section_sorted = sorted(num_list[82:87])
        return num_list_section_sorted[1]
    else:
        return None
