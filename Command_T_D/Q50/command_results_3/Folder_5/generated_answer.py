import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?P<text>[a-z]+){3}'.format(texts=texts), re.findall(r'(?i)(?P<name>[a-z]+){3}'.format(texts=texts), re.findall(r'(?i)(?P<word>[a-z]+){3}'.format(texts=texts)))))
