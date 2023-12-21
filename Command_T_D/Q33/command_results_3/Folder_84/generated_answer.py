import re
def return_vowels(s):
    return re.findall(r'([^BZIVOWXZJIOU])', s[770:852])
