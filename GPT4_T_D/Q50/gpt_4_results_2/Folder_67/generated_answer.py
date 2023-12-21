
def if_contains_anagrams(string_list):
    anagram_list = []
    for a in string_list:
        for b in string_list:
            if a.lower() != b.lower() and sorted(a.lower()) == sorted(b.lower()) and len(a) >= 3:
                anagram_list.append((a, b))
    
    if len(anagram_list) >= 41:
        return True
    else:
        return False
