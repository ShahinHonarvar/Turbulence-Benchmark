
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None

    second_smallest = None

    for i in range(len(my_list)):

        if my_list[i] < my_list[i + 1]:
            if second_smallest == None:
                second_smallest = my_list[i]

            else:

                if my_list[i] < second_smallest:
                    second_smallest = my_list[i]

    return second_smallest
