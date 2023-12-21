
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list, reverse=True)
    for i in range(52,71+1):
        if i >= len(sorted_list):
            return None
        largest_num = sorted_list[i]
        break
    second_largest_num = None
    for num in sorted_list:
        if num < largest_num and (second_largest_num is None or num > second_largest_num):
            second_largest_num = num
    return second_largest_num
