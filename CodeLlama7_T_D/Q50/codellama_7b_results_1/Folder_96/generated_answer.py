
def if_contains_anagrams(list_of_strings):
    # Count the number of anagram pairs in the list
    num_anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                num_anagram_pairs += 1
    # Return True if there are at least 98 anagram pairs in the list, otherwise False
    return num_anagram_pairs >= 98
