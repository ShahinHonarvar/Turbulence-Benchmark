
def find_second_largest_num(my_list):
    if len(my_list) < 3:
        return None

    second_largest = None

    for i in range(31, 35):

        if my_list[i] > second_largest or second_largest == None:

            second_largest = my_list[i]

    return second_largest
