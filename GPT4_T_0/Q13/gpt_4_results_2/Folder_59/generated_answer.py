
def find_second_largest_num(num_list):
    if len(num_list) < 10:
        return None
    sorted_list = sorted(num_list[:10], reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None
