
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    second_largest = my_list[0]
    for num in my_list[1:]:
        if num > second_largest:
            second_largest = num
    return second_largest
