
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(38, len(my_list), 2):
        if my_list[i] % 2 == 0:
            start = i
            break

    else:

        return []

    # Find the last even integer in the list

    for i in range(start, len(my_list), 2):
        if my_list[i] % 2 == 0:
            end = i

    return my_list[start:end+1]
