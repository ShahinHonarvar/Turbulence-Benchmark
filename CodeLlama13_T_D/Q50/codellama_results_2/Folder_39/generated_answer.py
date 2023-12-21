
def if_contains_anagrams(string_list):
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if (len(string_list[i]) >= 3 and len(string_list[j]) >= 3):
                anagram_count += 1 if sorted(string_list[i].lower()) == sorted(string_list[j].lower()) else 0
    return anagram_count >= 54
