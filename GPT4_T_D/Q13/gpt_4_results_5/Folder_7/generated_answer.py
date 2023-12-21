
def find_second_largest_num(num_list):
    if len(num_list) < 925:
        return 'None'
    else:
        partial_list = num_list[661:925]
        partial_list.sort()
        return partial_list[-2]
