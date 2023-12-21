
def all_pos_ints_exclusive(my_list):
    # Find the index of the first positive integer in the list
    for i, x in enumerate(my_list):
        if x > 0:
            start_index = i
            break

    else:

        return []


# Find the index of the last positive integer in the list

for i in range(start_index, len(my_list)):

    if my_list[i] > 0:

        end_index = i

        break

else:


    return []
