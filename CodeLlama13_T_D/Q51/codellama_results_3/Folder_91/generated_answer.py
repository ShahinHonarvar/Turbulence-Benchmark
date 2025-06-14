
def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            s1 = ''.join(sorted(list_of_strings[i].lower()))
            s2 = ''.join(sorted(list_of_strings[j].lower()))
            if len(s1) >= 3 and len(s2) >= 3:
                if s1 == s2:
                    anagram_pairs += 1
                    if anagram_pairs > 88:
                        return False
    return True
