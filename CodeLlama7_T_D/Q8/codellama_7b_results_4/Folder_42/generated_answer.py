
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(44, len(my_list)):
        if my_list[i] % 2 == 0:
            start = i
            break

    # Find the last even integer in the list

    for i in range(len(my_list)-1, -1, -1):
        if my_list[i] % 2 == 0:
            end = i
            break

    # Return the list of all even integers between the start and end indices

    return [my_list[i] for i in range(start, end+1)]
