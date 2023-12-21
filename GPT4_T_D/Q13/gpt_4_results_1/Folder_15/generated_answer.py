
def find_second_largest_num(num_list):
    try:
        first_four = sorted(num_list[:4], reverse=True)
        return first_four[1]
    except IndexError:
        return None
