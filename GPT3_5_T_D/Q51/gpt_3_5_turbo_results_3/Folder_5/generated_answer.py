
def if_contains_anagrams(str_lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagram_count = 0
    for i in range(len(str_lst)):
        for j in range(i + 1, len(str_lst)):
            if len(str_lst[i]) >= 3 and len(str_lst[j]) >= 3:
                if is_anagram(str_lst[i], str_lst[j]):
                    anagram_count += 1
                    if anagram_count > 4:
                        return False
    return True
