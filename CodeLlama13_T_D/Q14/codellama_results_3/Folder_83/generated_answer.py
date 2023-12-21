
def find_second_smallest_num(my_list):
    # Find the second smallest number in the list
    second_smallest = None
    for i in range(90, 201):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
