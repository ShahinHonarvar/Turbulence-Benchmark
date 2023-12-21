
def find_second_largest_num(numbers):
    try:
        sub_list = numbers[33:37]
        sub_list.sort()
        return sub_list[-2]
    except IndexError:
        return None
