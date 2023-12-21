
def if_contains_anagrams(list_of_strings):
    # Initialize an empty dictionary to store the anagram pairs
    anagram_pairs = {}

    # Loop through each string in the list
    for s in list_of_strings:
        # Convert the current string to lowercase
        s_lower = s.lower()

        # Check if the length of the current string is at least three
        if len(s_lower) >= 3:
            # If it is, sort the characters in the current string and use them as a key to access the anagram pairs dictionary
            sorted_chars = "".join(sorted(s_lower))
            if sorted_chars not in anagram_pairs:
                anagram_pairs[sorted_chars] = [s_lower]
            else:
                # If there are already anagrams for the current string, add the current string to the list of anagrams for that key
                anagram_pairs[sorted_chars].append(s_lower)

    # Check if there are at least 136 pairs of anagrams in the dictionary
    return len([key for key, val in anagram_pairs.items() if len(val) >= 2]) >= 136
