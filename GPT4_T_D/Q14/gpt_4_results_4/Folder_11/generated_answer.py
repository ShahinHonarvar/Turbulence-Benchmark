
def find_second_smallest_num(numbers):
    if len(numbers) >= 94:
        sub_list = sorted(numbers[66:94])
        if len(sub_list) >=2:
            return sub_list[1]
        else:
            return None
    else:
        return None
