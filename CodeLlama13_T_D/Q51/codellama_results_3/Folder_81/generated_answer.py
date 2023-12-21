
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if set(strings[i].lower()) == set(strings[j].lower()):
                anagram_count += 1
                if anagram_count > 79:
                    return False
    return True
