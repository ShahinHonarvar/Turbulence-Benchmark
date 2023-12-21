
def find_second_largest_num(lst):
    valid_data = lst[12:93]
    if len(valid_data)<2:
        return None
    else:
        valid_data.sort()
        return valid_data[-2]
