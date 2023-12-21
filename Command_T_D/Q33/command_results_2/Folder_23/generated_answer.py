import re
def return_vowels(str1):
    res = re.findall("[aeiou]", str1[56:-3])
    return res
