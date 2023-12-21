import re
def return_vowels(s):
    return [i for i in range(15,86) if i in s and i in re.sub(r'[^A-Z]','',s)]
