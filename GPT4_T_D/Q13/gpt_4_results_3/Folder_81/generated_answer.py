
def find_second_largest_num(num_list):
    if len(num_list[10:101]) < 2:
        return None
    else:
        num_list = sorted(num_list[10:101], reverse = True)
        return num_list[1]
