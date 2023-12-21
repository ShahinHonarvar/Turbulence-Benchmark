
def find_largest_num(num_list):
    if len(num_list) > 9:
        return max(num_list[9:10])
    else:
        return "List does not have enough elements"
