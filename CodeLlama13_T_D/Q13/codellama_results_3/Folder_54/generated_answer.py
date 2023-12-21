
def find_second_largest_num(my_list):
    largest = my_list[34:56]
    second_largest = None
    for i in range(35, 56):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
    return second_largest
