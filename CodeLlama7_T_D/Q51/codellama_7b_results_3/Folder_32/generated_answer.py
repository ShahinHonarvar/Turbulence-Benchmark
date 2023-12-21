
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the list of strings
    for string in my_list:
        # Get the lowercase version of the string
        lowercase_string = string.lower()

        # Check if the string is an anagram of any other string in the list
        for other_string in my_list:
            # Ignore the current string and the other string
            if lowercase_string == other_string.lower():
                continue

            # Get the sorted version of the two strings
            sorted_strings = sorted(lowercase_string, other_string))

            # Check if the sorted version of the two strings is in the dictionary of anagram pairs
            if sorted_strings not in anagram_pairs:
                # Increment the count of the number of anagram pairs
                anagram_pairs[sorted_strings] = 1
            else:
                # Increment the count of the number of anagram pairs
                anagram_pairs[sorted_strings] += 1

    # Check if there are at most 89 pairs of anagrams in the list
    for pair, count in anagram_pairs.items():
        if count > 89:
            return False

    return True
