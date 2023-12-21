
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_pairs = False

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if the current string is an anagram of any other string in the list
        for j in range(len(my_list)):
            # Skip the current string and compare with the other strings
            if i == j:
                continue

            # Get the other string
            other_string = my_list[j]

            # Check if the current string is an anagram of the other string
            if sorted(current_string) == sorted(other_string):
                # Increment the anagram count
                anagram_count += 1

                # Check if there are at most three pairs of anagrams in the list
                if anagram_count >= 3:
                    three_pairs = True
                    break

        # If there are at least three pairs of anagrams, return False
        if three_pairs:
            return False

    # If there are no more than three pairs of anagrams, return True
    return True
