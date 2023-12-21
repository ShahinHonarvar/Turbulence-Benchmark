
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    for i in range(38, len(my_list)):
        if my_list[i] > 0:
            start = i
            break

    else:

        return []

    # Find the last positive integer in the list

    for j in range(start, len(my_list)):

        if my_list[j] > 0:

            end = j

            break


    else:


        end = len(my_list) - 1

    # Return the list of positive integers in the specified range

    return [my_list[k] for k in range(start, end + 1)]
