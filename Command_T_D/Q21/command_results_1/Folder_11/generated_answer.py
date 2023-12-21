def all_ints_div_by_num(list):
    try:
        return [x for x in list[22:63] if x % -61 == 0]
    except:
        return []
