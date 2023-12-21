import re
def if_contains_anagrams(texts):
    return len(re.findall(r'(?i)(?P<str1>[a-z]){2,}(?P<str2>[a-z]){2,}(?P<str3>[a-z]){2,}\1(?i)(?P<str4>[a-z]){2,}(?P=str2)\2(?i)(?P=str3)\3(?i)(?P=str4)\4\1\2\3\4', texts)) <= 113
