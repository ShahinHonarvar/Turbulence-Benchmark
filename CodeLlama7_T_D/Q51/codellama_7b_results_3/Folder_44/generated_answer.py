
def if_contains_anagrams(strings):
    # Get the list of anagram pairs
    anagram_pairs = []
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            # Check if the strings are anagrams
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                # Add the pair to the list
                anagram_pairs.append((i, j)))
    # Check if there are at most 75 pairs of anagrams in the given list
    return len(anagram_pairs) <= 75
