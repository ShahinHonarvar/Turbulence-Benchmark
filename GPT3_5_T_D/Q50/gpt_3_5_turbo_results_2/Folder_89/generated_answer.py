
def if_contains_anagrams(strings):
    anagram_pairs_count = 0
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and strings[i].lower() == strings[j].lower() and sorted(strings[i].lower()) == sorted(strings[j].lower()):
                anagram_pairs_count += 1
                if anagram_pairs_count >= 36:
                    return True
    return False
