
def find_second_largest_num(num_list):
    if len(num_list) < 5:
        return None
    else:
        return sorted(num_list[4:5], reverse=True)[0] if len(num_list[4:5]) > 1 else None
