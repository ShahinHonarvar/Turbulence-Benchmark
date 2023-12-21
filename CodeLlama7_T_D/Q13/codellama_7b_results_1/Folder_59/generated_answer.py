
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    second_largest = None

    for i in range(len(my_list)):

        if my_list[i] > my_list[i - 1]:

            if second_largest == None:

                second_largest = my_list[i - 1]

            else:

                second_largest = max(my_list[i - 1], second_largest)

    return second_largest
