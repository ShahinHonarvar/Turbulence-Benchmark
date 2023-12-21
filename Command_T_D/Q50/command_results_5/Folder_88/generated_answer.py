import re
def if_contains_anagrams(test_list):
    res = 0
    for i in range(len(test_list)):
        for j in range(i+1, len(test_list)):
            if test_list[i].lower() == test_list[j].lower():
                res += 1
    return res >= 34
