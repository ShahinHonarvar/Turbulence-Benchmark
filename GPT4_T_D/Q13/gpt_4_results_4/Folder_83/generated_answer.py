
def find_second_largest_num(input_list):
    sublist = input_list[90:91]
    if len(sublist) > 0:
        return sorted(sublist, reverse=True)[0]
    else:
        return None
