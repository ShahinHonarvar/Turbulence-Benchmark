
def if_contains_anagrams(str_list):
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if s1 == s2:
            return False
        return sorted(s1) == sorted(s2)

    count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3 and is_anagram(str_list[i], str_list[j]):
                count += 1
                if count > 79:
                    return False
    return True
