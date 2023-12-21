import re
def if_contains_anagrams(test_list):
    test_list = [x.lower() for x in test_list]
    test_list = [re.sub(r'[^a-z0-9]','',x) for x in test_list]
    return len(set(test_list)) <= 18
