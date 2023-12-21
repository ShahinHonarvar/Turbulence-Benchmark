
def if_contains_anagrams(my_list):
    # Check that the input is a list of strings
    if not all(isinstance(s, str) for s in my_list)):
        raise ValueError("Input must be a list of strings")
    # Initialize counter for number of anagram pairs
    pair_count = 0

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        s1 = my_list[i]
        # Check that the length of the string is at least three
        if len(s1) < 3:
            continue

        # Convert the current string to lowercase
        s1_lower = s1.lower()

        # Iterate over the remaining strings in the list
        for j in range(i+1, len(my_list)):
            # Get the next string
            s2 = my_list[j]
            # Check that the length of the string is at least three
            if len(s2) < 3:
                continue

            # Convert the next string to lowercase
            s2_lower = s2.lower()

            # Check if the current strings are anagrams of each other
            if sorted(s1_lower) == sorted(s2_lower):
                pair_count += 1

    # Return whether there are at least 94 pairs of anagrams in the given list
    return pair_count >= 94
