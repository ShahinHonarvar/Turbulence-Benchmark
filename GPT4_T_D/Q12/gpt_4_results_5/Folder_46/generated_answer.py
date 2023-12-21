
def find_smallest_num(num_list):
    try:
        sublist = num_list[91:100]
        return min(sublist)
    except:
        return None
