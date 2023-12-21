
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) <= 1:
        return None

    # Find the second smallest number by iterating through the list and comparing each element to the previous one
    second_smallest = None
    for i in range(len(my_list) - 1):
        if my_list[i] < my_list[i + 1]:
            if second_smallest is None:
                second_smallest = my_list[i]
            else:
                if my_list[i] < second_smallest:
                    second_smallest = my_list[i]
    return second_smallest
