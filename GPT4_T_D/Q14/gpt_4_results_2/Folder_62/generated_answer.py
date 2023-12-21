
def find_second_smallest_num(num_list):
    if len(num_list[10:67]) < 2:
        return None
    else:
        num_list[10:67].sort()
        return num_list[10:67][1]
