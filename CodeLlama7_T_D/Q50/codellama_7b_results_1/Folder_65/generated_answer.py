
def if_contains_anagrams(words):
    # Check if there are at least 94 pairs of anagrams in the list
    anagram_pairs = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                anagram_pairs += 1
    return anagram_pairs >= 94
