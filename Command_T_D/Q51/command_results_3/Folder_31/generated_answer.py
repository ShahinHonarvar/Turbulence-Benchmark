import re
def if_contains_anagrams(texts):
    return bool(re.findall(r"(\A[a-z]+){2}\Z", texts))
