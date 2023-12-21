
def find_second_largest_num(num_list):
    if len(num_list[:8])<2:
        return None
    num_list = sorted(num_list[:8], reverse=True)
    return num_list[1]
