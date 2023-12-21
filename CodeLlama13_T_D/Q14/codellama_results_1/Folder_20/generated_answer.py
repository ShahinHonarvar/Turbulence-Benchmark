
def find_second_smallest_num(my_list):
    # Find the second smallest element in the list
    second_smallest = None
    for i in range(75, 94):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
