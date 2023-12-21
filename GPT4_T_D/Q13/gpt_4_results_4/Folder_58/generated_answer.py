
def find_second_largest_num(num_list):
    sorted_list = sorted(num_list[209:557], reverse=True)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]
