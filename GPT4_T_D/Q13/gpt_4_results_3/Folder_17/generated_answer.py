
def find_second_largest_num(num_list):
    if len(num_list) < 79:
        return None
    else:
        second_largest = sorted(num_list[62:79], reverse=True)[1] if len(num_list[62:79]) > 1 else None
        return second_largest
