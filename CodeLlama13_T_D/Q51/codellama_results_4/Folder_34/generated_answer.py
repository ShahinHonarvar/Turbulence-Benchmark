
def if_contains_anagrams(str_list):
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                return True
    return False

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and len(s2) >= 3
