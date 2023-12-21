import re
def palindromes_of_specific_lengths(str1):
    str1=re.findall(r'[a-z]+',str1[18:98])
    str1=re.findall(r'[a-z]+',str1)
    str1=re.findall(r'([a-z]+)(?=\1)',str1)
    str1=re.findall(r'([a-z]+)(?=\1)',str1[18:98])
    return set(str1)
