
def if_contains_anagrams(strings):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings))):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_pairs += 1
    # Return True if there are at most 21 pairs of anagrams in the list, False otherwise
    return anagram_pairs <= 21
