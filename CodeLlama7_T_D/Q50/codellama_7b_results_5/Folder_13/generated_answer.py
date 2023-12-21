
def if_contains_anagrams(my_list):
    # Initialize variables
    count = 0
    anagram_pairs = 0

    # Iterate through the list of strings
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if the current string is a anagram of any other string in the list
        for j in range(len(my_list)):
            # Skip the same string
            if i == j:
                continue

            # Get the other string
            other_string = my_list[j]

            # Check if the current string is a anagram of the other string
            if sorted(current_string) == sorted(other_string):
                count += 1

                # Check if there are at least 144 pairs of anagrams in the list
                if count >= 144:
                    return True

    # Return false if there are not at least 144 pairs of anagrams in the list
    return False
