
def find_second_largest_num(num_list):
    if num_list[66:94]:
        sorted_list = sorted(num_list[66:94])
        return sorted_list[-2] if len(sorted_list) > 1 else None
    else:
        return None
