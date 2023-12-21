
def find_second_largest_num(numbers):
    if len(numbers)<74:
        return None
    else:
        sorted_sublist = sorted(numbers[74:96], reverse=True)
        if len(sorted_sublist) < 2:
            return None
        else:
            return sorted_sublist[1]
