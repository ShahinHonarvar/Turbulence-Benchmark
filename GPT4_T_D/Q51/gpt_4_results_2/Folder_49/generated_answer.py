
def if_contains_anagrams(string_list):
    anagram_pairs = []
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) != len(string_list[j]) or len(string_list[i]) < 3:
                continue
            if sorted(string_list[i].lower()) == sorted(string_list[j].lower()):
                anagram_pairs.append((string_list[i], string_list[j]))
    if len(anagram_pairs) > 10:
        return False
    else:
        return True
