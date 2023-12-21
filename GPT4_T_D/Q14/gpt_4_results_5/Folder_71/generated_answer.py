
def find_second_smallest_num(num_list):
    portion_list = num_list[29:52]
    if len(portion_list) <= 1:
        return None
    else:
        portion_list.sort()
        return portion_list[1]
