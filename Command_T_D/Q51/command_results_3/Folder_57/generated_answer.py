import re
def if_contains_anagrams(list1):
    list1 = re.findall(r'(?i)([a-z]+)', list1)
    list1 = set(list1)
    if len(list1) == len(list(filter(lambda x: len(x) >= 3, list1))):
        return True
    else:
        return False
