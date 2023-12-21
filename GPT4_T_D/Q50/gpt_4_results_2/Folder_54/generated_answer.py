
def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            string1 = ''.join(sorted(string_list[i].lower()))
            string2 = ''.join(sorted(string_list[j].lower()))
            if string1 == string2 and len(string1) >= 3:
                anagram_pairs += 1
    return anagram_pairs >= 74
