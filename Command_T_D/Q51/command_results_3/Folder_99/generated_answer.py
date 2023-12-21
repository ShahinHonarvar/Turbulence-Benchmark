import re
def if_contains_anagrams(test_list):
    res = 0
    for i in range(len(test_list)):
        for j in range(i+1,len(test_list)):
            if re.match(r'(?i)(?=.*'.join(sorted(test_list[i])), test_list[j], re.I) is None:
                res += 1
            if res > 93:
                return False
    return True
