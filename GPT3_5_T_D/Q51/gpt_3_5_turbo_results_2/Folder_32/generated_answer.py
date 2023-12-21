
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    anagram_count += 1
                    if anagram_count > 89:
                        return False
    return True
