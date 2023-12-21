
def if_contains_anagrams(str_list):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower()) and len(str1) >= 3

    count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                count += 1
                if count >= 155:
                    return True
    return False
