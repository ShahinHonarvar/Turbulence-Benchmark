def all_ints_div_by_num(int_list):
    int_list = [e for e in int_list if e%58==0]
    return [e for e in int_list if e>=62 and e<=70]
