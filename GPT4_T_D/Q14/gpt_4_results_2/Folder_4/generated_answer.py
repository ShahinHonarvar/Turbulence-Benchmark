
def find_second_smallest_num(num_list):
    if len(num_list) < 85:
        return None
    temp_list = sorted(num_list[70:85])
    if len(temp_list) < 2:
        return None
    else:
        return temp_list[1]
