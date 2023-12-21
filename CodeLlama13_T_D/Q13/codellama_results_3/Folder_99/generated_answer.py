
def find_second_largest_num(my_list):
    second_largest = None
    largest = my_list[310:371][-1]
    for i in range(310, 371):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
    return second_largest
