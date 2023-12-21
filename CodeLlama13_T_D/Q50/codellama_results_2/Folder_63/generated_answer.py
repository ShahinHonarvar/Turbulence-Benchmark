
def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            if len(set(list_of_strings[i].lower())) >= 3 and len(set(list_of_strings[j].lower())) >= 3:
                if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                    anagram_pairs += 1
                    if anagram_pairs >= 89:
                        return True
    return False
