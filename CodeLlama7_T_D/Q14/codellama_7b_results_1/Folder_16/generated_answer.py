 def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = my_list[66]
    for i in range(67, 78):
        if my_list[i] < smallest:
            smallest = my_list[i]
    # Check if there is a second smallest element

    if len(my_list) > 77:
        return None

    else:

        for i in range(66, 77):

            if my_list[i] == smallest:
                return my_list[i + 1]

        return None
