import re
def return_vowels(string):
    res = re.findall("[aeiou][^pz]", string)
    return res
