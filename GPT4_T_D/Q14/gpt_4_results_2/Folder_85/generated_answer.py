
def find_second_smallest_num(num_list):
    try:
        sliced_list = num_list[0:7]
        sliced_list.sort()
        return sliced_list[1] if len(sliced_list) > 1 else None
    except:
        return None
