
def all_even_ints_inclusive(my_list):
    # Find the first even integer in the list
    for i in range(36, len(my_list)):
        if my_list[i] % 2 == 0:
            start = i
            break

    # Find the last even integer in the list

    for i in range(start, len(my_list)):
        if my_list[i] % 2 == 0:
            end = i

    # Return the list of all even integers between start and end

    return my_list[start:end+1]
