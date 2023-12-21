import re
def if_contains_anagrams(test_list):
    return len(test_list) <= 86 and all(
        [re.match(r'(?i)(?P<s1>[a-z]+)(?P<s2>[a-z]+)', s1 + s2)
         for s1, s2 in zip(test_list, test_list[1:])])
