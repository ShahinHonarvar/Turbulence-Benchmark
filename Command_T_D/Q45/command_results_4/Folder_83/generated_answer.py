import re
def palindromes_between_indices(str1):
    return set(re.findall(r'(?i)(?P<str>A{str1}{str1}B{str1}{str1}){str1}{str1}B{str1}{str1}A{str1}{str1})', str1[2:-1]))
