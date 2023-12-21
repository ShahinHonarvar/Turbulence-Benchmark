
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3:
                anagram_pairs += 1
                if anagram_pairs > 19:
                    return False
    return True
