
def if_contains_anagrams(word_list):
    # Get the list of anagram pairs
    anagram_pairs = []
    for i in range(len(word_list) - 1):
        for j in range(i + 1, len(word_list))):
            if sorted(word_list[i]) == sorted(word_list[j])):
                anagram_pairs.append((i, j)))
    # Check the number of anagram pairs
    num_anagram_pairs = len(anagram_pairs)
    # Return True if there are at most 2 pairs of anagrams in the list
    return num_anagram_pairs <= 2
