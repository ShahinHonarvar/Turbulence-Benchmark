
def if_contains_anagrams(str_list):
    anagram_count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                anagram_count += 1
                if anagram_count >= 177:
                    return True
    return False

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
