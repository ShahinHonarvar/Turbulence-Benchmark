 def find_second_largest_num(my_list):
    # Find the index of the second largest element in the list
    my_list = sorted(my_list)
    index_25 = my_list.index(my_list[24]) + 1
    index_87 = my_list.index(my_list[86]) + 1
    # Check if the second largest element is between indices 25 and 87
    for i in range(index_25, index_87 + 1):
        # If the current element is larger than the previous one, return it
        if my_list[i] > my_list[i - 1]:
            return my_list[i]
