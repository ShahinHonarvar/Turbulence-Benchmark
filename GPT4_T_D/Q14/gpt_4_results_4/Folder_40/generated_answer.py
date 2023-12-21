
def find_second_smallest_num(num_list):
    try:
        truncated_list = num_list[0:3]
        truncated_list.sort()
        if len(truncated_list) >= 2:
            return truncated_list[1]
        else:
            return None
    except:
        return None
