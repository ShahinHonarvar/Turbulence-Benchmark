
def if_contains_anagrams(my_list):
    # Create a dictionary to store the number of anagrams for each length
    anagram_lengths = {}

    # Loop through the list of strings and count the number of anagrams for each length
    for string in my_list:
        length = len(string)
        if length not in anagram_lengths:
            anagram_lengths[length] = 0

        anagram_lengths[length] += len(set(string.lower())))

    # Check if there are at most 85 pairs of anagrams for each length
    for length in anagram_lengths:
        if anagram_lengths[length] > 85:
            return False

    return True
