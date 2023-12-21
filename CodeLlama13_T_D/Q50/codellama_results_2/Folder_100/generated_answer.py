
def if_contains_anagrams(my_list):
    anagram_count = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            s1 = ''.join(sorted(my_list[i].lower()))
            s2 = ''.join(sorted(my_list[j].lower()))
            if s1 == s2 and len(s1) >= 3:
                anagram_count += 1
    return anagram_count >= 95
