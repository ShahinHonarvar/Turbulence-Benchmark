import re
def if_contains_anagrams(test_list):
    res = 0
    for i in range(len(test_list)):
        for j in range(i + 1, len(test_list)):
            s1 = test_list[i]
            s2 = test_list[j]
            s1_lower = s1.lower()
            s2_lower = s2.lower()
            if re.match(s1_lower, s2_lower):
                res += 1
    return res >= 65
