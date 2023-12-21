
def find_second_smallest_num(num_list):
    try:
        chunk = num_list[43:52]
        if len(chunk) < 2:
            return None
        return sorted(chunk)[1]
    except IndexError:
        return None
