
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    largest = my_list[0]
    second_largest = None
    for i in range(1, min(8, len(my_list))):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif second_largest is None or my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
