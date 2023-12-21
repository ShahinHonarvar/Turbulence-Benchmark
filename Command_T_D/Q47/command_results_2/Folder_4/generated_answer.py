import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r"<(?P<s>[a-z]+?)(?P<e>[a-z]+?)>", text, flags=re.IGNORECASE))
