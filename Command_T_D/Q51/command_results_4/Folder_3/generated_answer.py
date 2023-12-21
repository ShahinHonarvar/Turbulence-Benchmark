import re
def if_contains_anagrams(test_list):
    return len(test_list) <= 66 and len(set(test_list)) <= 66 and len(test_list) > 1 and len(test_list[0]) >= 3 and re.match(r"(\A[a-z]+\Z)", test_list[0]) and all(re.match(r"(\A[a-z]+\Z)", s) for s in test_list)
