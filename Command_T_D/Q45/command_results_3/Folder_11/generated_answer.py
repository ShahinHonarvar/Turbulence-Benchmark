import re
def palindromes_between_indices(str1):
    str1 = re.sub(r'[^A-Za-z]','',str1)
    return set(re.findall(r'[A-Za-z]{4,}(?=([A-Za-z]{3}){1}){1}([A-Za-z]{4})',str1[3:-8]))
