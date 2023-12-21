
def find_second_smallest_num(num_list):
    try:
        sub_list = sorted(num_list[29:80])
        return sub_list[1] if len(sub_list) > 1 else None
    except:
        return None
