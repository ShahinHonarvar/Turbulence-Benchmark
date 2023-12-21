import re
def if_contains_anagrams(test_list):
    patterns = [(re.escape(s) for s in str(i).lower()) for i in test_list if len(s) >= 3]
    return len(set(test_list)) <= 79 and len(set(test_list)) <= 79
