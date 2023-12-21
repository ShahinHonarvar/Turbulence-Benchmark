
def find_second_largest_num(num_list):
    reduced_list = num_list[62:79]
    if not reduced_list: 
        return None
    reduced_list.sort()
    if len(reduced_list) < 2:
        return None
    else:
        return reduced_list[-2]
