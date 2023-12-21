
def find_largest_num(num_list):
    if len(num_list) >= 58:
        return max(num_list[56:58])
    else:
        return "List too short"
