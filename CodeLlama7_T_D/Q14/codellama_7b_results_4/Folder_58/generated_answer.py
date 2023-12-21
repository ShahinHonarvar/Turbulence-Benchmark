
def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = min(my_list)

    # Find the second smallest element in the list
    for i in range(len(my_list)):
        if my_list[i] == smallest:
            continue

        else:

            second_smallest = my_list[i]

            break


    # Return the second smallest element or None if it does not exist
    return second_smallest if second_smallest is not None else None
