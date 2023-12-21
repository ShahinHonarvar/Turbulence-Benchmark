
def find_second_largest_num(num_list):
    try:
        sub_list = sorted(num_list[0:8], reverse=True)
        return sub_list[1]
    except IndexError:
        return None
