
def if_contains_anagrams(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) <= 1:
        return False

    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the list of strings
    for string in my_list:

        # Convert the string to lowercase and sort the characters
        sorted_chars = ''.join(sorted(string.lower()))

        # If the sorted string is already in the dictionary, increment its count by 1
        if sorted_chars in anagram_pairs:
            anagram_pairs[sorted_chars] += 1

        # Otherwise, add the sorted string to the dictionary with a count of 1
        else:
            anagram_pairs[sorted_chars] = 1

    # Iterate over the dictionary of anagram pairs
    for pair in anagram_pairs:

        # Check if the current pair has at least three elements
        if anagram_pairs[pair] >= 3:

            # If so, check if there are at most 36 pairs of anagrams in the list
            if len(anagram_pairs) <= 36:
                return True

    # If none of the conditions above are met, return false
    return False
