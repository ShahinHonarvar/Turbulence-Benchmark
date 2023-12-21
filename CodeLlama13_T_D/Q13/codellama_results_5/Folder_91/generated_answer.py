
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    largest = my_list[0]
    second_largest = None

    for i in range(1, len(my_list)):
        current = my_list[i]
        if current > largest:
            second_largest = largest
            largest = current
        elif second_largest is None or current > second_largest:
            second_largest = current
    return second_largest
