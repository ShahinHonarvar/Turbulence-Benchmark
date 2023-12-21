
def if_contains_anagrams(strings):
    anagram_pairs = []
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_pairs.append((i, j))
    return len(anagram_pairs) >= 7
