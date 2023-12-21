
def lists_with_product_equal_n(circular_list, n):
    # Create an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find the first integer that is equal to n

    for i in range(len(circular_list)):
        if circular_list[i] == n:
            # Create a new sublist with the first integer that is equal to n

            sublists.append([circular_list[i]])

            # Iterate through the remaining integers in the circular list and find the contiguous sequence of integers whose product is equal to n

            for j in range(i + 1, len(circular_list)):
                if circular_list[j] == n:
                    sublists[-1].append(circular_list[j])

                    # If the length of the current sublist is greater than or equal to the size of the given list, then break out of the loop

                    if len(sublists[-1]) >= len(circular_list):
                        break

            # If the length of the current sublist is less than the size of the given list, then there are still more integers in the circular list that can be added to the sublist

            if len(sublists[-1]) < len(circular_list):
                continue

            # If the length of the current sublist is greater than or equal to the size of the given list, then break out of the loop

            else:
                break

    # Return the list of sublists that were found

    return sublists
