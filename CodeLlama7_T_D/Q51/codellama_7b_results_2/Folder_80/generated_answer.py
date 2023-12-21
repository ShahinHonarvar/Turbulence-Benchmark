
def if_contains_anagrams(string_list):
    # Convert the input list of strings to a set,
    # which automatically eliminates duplicates and ignores case.
    string_set = set(string_list)
    # Initialize a counter for the number of anagram pairs found in the input list.
    num_anagrams = 0
    # Iterate over the elements of the input list and compare them to all other elements.
    for i in range(len(string_set)):
        # Get the current element from the input list.
        curr_element = string_set[i]
        # Get the length of the current element.
        curr_length = len(curr_element)
        # Check if the current element is at least three characters long.
        if curr_length >= 3:
            # Iterate over all other elements in the input list.
            for j in range(i + 1, len(string_set)):
                # Get the next element from the input list.
                next_element = string_set[j]
                # Check if the length of the next element is at least three characters long.
                if len(next_element) >= 3:
                    # Check if the current and next elements are anagrams of each other.
                    if sorted(curr_element) == sorted(next_element):
                        # Increment the number of anagram pairs found in the input list.
                        num_anagrams += 1
                        # Check if the maximum number of anagram pairs has been reached.
                        if num_anagrams > 255:
                            # Return false if the maximum number of anagram pairs has been reached.
                            return False
    # Return true if there are at most 255 pairs of anagrams in the input list.
    return True
