
def if_contains_anagrams(string_list):
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) == len(string_list[j]) and sorted(string_list[i].lower()) == sorted(string_list[j].lower()):
                anagram_count += 1
            if anagram_count > 113:
                return False
    return True
