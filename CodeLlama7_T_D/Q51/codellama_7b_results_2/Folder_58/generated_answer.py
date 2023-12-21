
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize a counter for the number of pairs of anagrams
    pair_counter = 0

    # Iterate over the elements in the list
    for i in range(len(my_list)):
        # Get the current element
        current_element = my_list[i]

        # Check if the current element is a string
        if isinstance(current_element, str):
            # Convert the current element to lowercase
            current_element = current_element.lower()

            # Get the sorted version of the current element
            sorted_current_element = ''.join(sorted(current_element))

            # Iterate over the remaining elements in the list
            for j in range(i + 1, len(my_list)):
                # Get the next element
                next_element = my_list[j]

                # Check if the next element is a string
                if isinstance(next_element, str):
                    # Convert the next element to lowercase
                    next_element = next_element.lower()

                    # Get the sorted version of the next element
                    sorted_next_element = ''.join(sorted(next_element))

                    # Check if the sorted versions of the current and next elements are equal
                    if sorted_current_element == sorted_next_element:
                        # Increment the pair counter
                        pair_counter += 1

                        # If there are at most 60 pairs of anagrams in the list, return True
                        if pair_counter <= 60:
                            return True

    # If there are no more than 60 pairs of anagrams in the list, return False
    return False
