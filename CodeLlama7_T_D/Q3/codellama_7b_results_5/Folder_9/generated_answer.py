
def all_pos_ints_inclusive(my_list):
    start = 70
    end = 200
    return [x for x in my_list[start:end+1] if x > 0]
