
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3:
                anagram_count += 1
                if anagram_count > 14:
                    return False
    return True
