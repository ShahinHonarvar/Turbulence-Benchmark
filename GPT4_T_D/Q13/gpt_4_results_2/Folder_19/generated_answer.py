
def find_second_largest_num(num_list):
    try:
        sliced_list = sorted(num_list[3:6], reverse=True)
        return sliced_list[1]
    except IndexError:
        return None
