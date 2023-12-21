
def if_contains_anagrams(str_list):
    anagram_count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if (sorted(str_list[i].lower()) == sorted(str_list[j].lower())) and (len(str_list[i]) >= 3):
                anagram_count += 1
                if anagram_count > 173:
                    return False
    return True
