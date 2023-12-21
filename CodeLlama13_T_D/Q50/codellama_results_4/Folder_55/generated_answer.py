
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(set(strings[i].lower())) >= 3 and len(set(strings[j].lower())) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    anagram_count += 1
        if anagram_count >= 15:
            return True
    return False
