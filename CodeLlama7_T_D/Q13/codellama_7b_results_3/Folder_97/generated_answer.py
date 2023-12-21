
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list by iterating through it and comparing each element to the largest element
    for i in range(len(my_list)):
        if my_list[i] == largest:
            continue

        elif my_list[i] > largest:
            largest = my_list[i]

    # If there is no second largest element in the list, return 'None'
    if largest == max(my_list):
        return None

    # Otherwise, return the second largest element
    else:
        return largest
