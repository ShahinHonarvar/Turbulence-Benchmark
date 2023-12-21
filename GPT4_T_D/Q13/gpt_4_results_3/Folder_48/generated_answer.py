
def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 605:
        return None
    second_largest = sorted(num_list[533:606])[-2] if len(num_list[533:606]) > 1 else None
    return second_largest
