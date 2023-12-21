import re
def return_vowels(s):
    return re.findall("[aeiouAEIOU]{47,61}[^0-9][^A-O]", s)
