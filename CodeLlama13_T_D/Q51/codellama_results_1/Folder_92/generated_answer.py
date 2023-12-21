
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = strings[i].lower()
            s2 = strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    anagram_count += 1
            if anagram_count > 34:
                return False
        else:
            continue
    return True
