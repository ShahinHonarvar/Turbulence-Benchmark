
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    for i in range(len(my_list) - 1)):
        # Check if there are at least 38 pairs of anagrams in the given list
        if len(anagram_pairs) >= 38:
            return True

        # Compare the strings in a case-insensitive manner
        if my_list[i].lower() == my_list[i + 1].lower():
            # If there is a pair of anagrams, add it to the dictionary
            anagram_pairs[(my_list[i], my_list[i + 1])] = True

    return False
