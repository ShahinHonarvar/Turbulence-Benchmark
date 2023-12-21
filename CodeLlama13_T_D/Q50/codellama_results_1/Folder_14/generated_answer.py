
def if_contains_anagrams(string_list):
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(set(string_list[i].lower())) >= 3 and len(set(string_list[j].lower())) >= 3:
                if set(string_list[i].lower()) == set(string_list[j].lower()):
                    anagram_count += 1
            if anagram_count >= 22:
                return True
    return False
