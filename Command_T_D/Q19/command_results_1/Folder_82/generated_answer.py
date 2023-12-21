def all_ints_not_div_by_num(num_list):
    try:
        return [x for x in num_list[20:200] if x % 200 != num_list[0]]
    except:
        return []
