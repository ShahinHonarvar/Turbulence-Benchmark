import re
def return_vowels(str1):
    res = re.findall("[AEIOU][^p{17}AEIOU]{17,62}", str1)
    return res
