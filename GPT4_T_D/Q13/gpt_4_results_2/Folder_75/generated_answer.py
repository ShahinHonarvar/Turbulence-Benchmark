
def find_second_largest_num(numbers):
    try:
        sub_list = sorted(numbers[56:58], reverse=True)
        return sub_list[1] if len(sub_list) > 1 else None
    except IndexError:
        return None
