
def if_contains_anagrams(string_list):
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1) == sorted(s2)
    
    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                count += 1
                if count > 39:
                    return False
    return True
