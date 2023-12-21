import re
def palindromes_of_specific_lengths(str1):
    str1 = str1[29:-29]
    str1 = re.sub(r'[^A-Za-z]+', '', str1)
    str1 = str1.lower()
    return set(re.findall(r'[a-z]+\d{4}[a-z]+', str1))
