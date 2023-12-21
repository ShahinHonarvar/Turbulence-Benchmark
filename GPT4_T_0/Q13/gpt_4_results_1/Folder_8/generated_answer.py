
def find_second_largest_num(num_list):
    if len(num_list) < 24:
        return None
    else:
        return sorted(num_list[23:24], reverse=True)[0] if len(num_list[23:24]) > 1 else None
