
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 29:
                    return False

    return True
