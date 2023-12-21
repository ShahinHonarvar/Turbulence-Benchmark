
def all_pos_ints_exclusive(my_list):
    start = 56
    end = 92
    if len(my_list) < start or len(my_list) < end:
        return []

    else:

        return [x for x in my_list[start:end] if x > 0]
