
def if_contains_anagrams(string_list):
    anagram_count = 0
    for i in range(len(string_list)):
        str1 = string_list[i].lower()
        for j in range(i+1, len(string_list)):
            str2 = string_list[j].lower()
            if str1 != str2 and sorted(str1) == sorted(str2):
                anagram_count += 1
                break
    return anagram_count >= 15
