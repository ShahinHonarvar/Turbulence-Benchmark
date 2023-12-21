
def find_second_largest_num(numbers):
    if len(numbers[29:80]) < 2:
        return None
    sub_list = sorted(numbers[29:80], reverse=True)
    return sub_list[1]
