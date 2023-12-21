
def find_second_largest_num(num_list):
    temp_list = sorted(num_list[0:6], reverse=True)
    if len(temp_list) > 1:
        return temp_list[1]
    else:
        return None
