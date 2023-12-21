def all_ints_div_by_num(int_list):
    try:
        result = []
        for i in range(6, 8):
            if int_list[i] % -9 == 0:
                result.append(int_list[i])
        return result
    except:
        return []
