
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        for j in range(i+1, len(strings)):
            if len(strings[j]) < 3:
                continue
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                anagram_count += 1
                if anagram_count > 5:
                    return False
    return True
