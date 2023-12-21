
def find_second_largest_num(num_list):
    if len(num_list) < 87:
        return None
    else:
        shortened_list = num_list[43:87]
        shortened_list.sort()
        return shortened_list[-2] if len(shortened_list) >= 2 else None
