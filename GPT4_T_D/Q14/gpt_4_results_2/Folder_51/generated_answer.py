
def find_second_smallest_num(num_list):
    try:
        sliced_list = num_list[1:9]
        if len(sliced_list)<2:
            return None
        else:
            sliced_list.sort()
            return sliced_list[1]
    except:
        return None
