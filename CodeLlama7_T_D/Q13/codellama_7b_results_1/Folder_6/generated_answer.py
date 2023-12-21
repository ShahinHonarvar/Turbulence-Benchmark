
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    largest = my_list[0]
    second_largest = None

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]

    if second_largest is not None:
        return second_largest

    else:

        return None
