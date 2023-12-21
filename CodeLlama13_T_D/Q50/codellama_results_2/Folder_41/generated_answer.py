
def if_contains_anagrams(str_list):
    anagram_count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str_a = str_list[i].lower()
            str_b = str_list[j].lower()
            if len(str_a) >= 3 and len(str_b) >= 3:
                if sorted(str_a) == sorted(str_b):
                    anagram_count += 1
    return anagram_count >= 75
