
def find_second_smallest_num(numbers_list):
    try:
        sub_list = sorted(numbers_list[66:94])
        if len(sub_list) >= 2:
            return sub_list[1]
        else:
            return None
    except (TypeError, ValueError):
        return None
