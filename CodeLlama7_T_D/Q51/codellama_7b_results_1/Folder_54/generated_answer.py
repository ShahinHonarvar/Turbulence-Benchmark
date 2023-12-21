
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Create a set of all anagram pairs in the list
    anagram_pairs = set()
    for word1 in my_list:
        for word2 in my_list:
            # Skip if both words are the same or one is a prefix of the other
            if word1 == word2 or word1.startswith(word2):
                continue

            # Check if the two words are anagrams
            if sorted(word1) == sorted(word2):
                anagram_pairs.add((word1, word2))

    # Return True if there are at most 39 pairs of anagrams in the list
    return len(anagram_pairs) <= 39
