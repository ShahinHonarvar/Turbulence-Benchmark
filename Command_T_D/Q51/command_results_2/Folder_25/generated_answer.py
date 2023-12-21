import re
def if_contains_anagrams(test_list):
    test_list = [re.sub(r'[A-Z]', '', str(i)).lower() for i in test_list]
    return len(set(test_list)) <= 67
