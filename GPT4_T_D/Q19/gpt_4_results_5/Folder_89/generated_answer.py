
def all_ints_not_div_by_num(int_list):
    selected_ints = int_list[49:62]
    result = [i for i in selected_ints if i%28 != 0]
    return result
