
def find_second_smallest_num(number_list):
    subset = number_list[8:10]
    if len(subset) < 2:
        return None
    else:
        return sorted(subset)[1]
