 
import re
def return_vowels(s):
    res = re.findall(r'[aeiou](?=[\W_])', s)
    return res
