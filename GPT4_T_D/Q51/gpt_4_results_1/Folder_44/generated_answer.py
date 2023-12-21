
def if_contains_anagrams(list_strings):
    anagram_pairs = []
    for i in range(len(list_strings)):
        for j in range(i+1,len(list_strings)):
            if len(list_strings[i]) >= 3 and len(list_strings[j]) >= 3:
                if sorted(list_strings[i].lower()) == sorted(list_strings[j].lower()):
                    anagram_pairs.append((list_strings[i], list_strings[j]))
    if len(anagram_pairs) <= 75:
        return True
    else:
        return False
