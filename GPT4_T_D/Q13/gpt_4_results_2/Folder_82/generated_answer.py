
def find_second_largest_num(num_list):
    if len(num_list) < 201:
        return None
    else:
        return sorted(num_list[20:201], reverse=True)[1]
