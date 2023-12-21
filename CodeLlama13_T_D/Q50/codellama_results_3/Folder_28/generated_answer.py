
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if set(strings[i].lower()) == set(strings[j].lower()):
                anagram_pairs += 1
                if anagram_pairs >= 81:
                    return True
    return False
