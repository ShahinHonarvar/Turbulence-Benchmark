
def find_second_smallest_num(num_list):
    try:
        return sorted(num_list[0:6])[1]
    except:
        return None
