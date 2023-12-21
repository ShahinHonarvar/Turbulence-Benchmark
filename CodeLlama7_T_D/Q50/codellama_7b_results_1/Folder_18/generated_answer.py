
def if_contains_anagrams(str_list):
    anagram_count = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                anagram_count += 1
    return anagram_count >= 106
