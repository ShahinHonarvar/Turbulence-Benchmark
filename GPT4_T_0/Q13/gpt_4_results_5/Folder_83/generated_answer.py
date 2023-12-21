
def find_second_largest_num(num_list):
    if len(num_list) < 91:
        return None
    else:
        return sorted(num_list[90:91], reverse=True)[0] if len(num_list[90:91]) > 1 else None
