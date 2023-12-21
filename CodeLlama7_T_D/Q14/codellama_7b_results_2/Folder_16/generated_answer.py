
def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = min(my_list)

    # Find the second smallest element in the list
    for i in range(len(my_list)):
        if my_list[i] == smallest:
            continue

        elif my_list[i] < smallest:
            smallest = my_list[i]

    # If there is no second smallest element, return 'None'
    if len(my_list) - my_list.count(smallest) <= 1:
        return None

    # Otherwise, return the second smallest element
    else:
        return smallest
