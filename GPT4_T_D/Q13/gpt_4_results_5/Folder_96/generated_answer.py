
def find_second_largest_num(num_list):
    try:
        index_list = num_list[15:52]
        index_list.sort(reverse=True)
        return index_list[1]
    except:
        return None
