
def find_second_smallest_num(num_list):
    if len(num_list[608:610]) < 2:
        return None
    else:
        return sorted(num_list[608:610])[1]
