 
import re
def return_vowels(text):
    res = re.findall(r'[aeiou]', text[770:852])
    return list(filter(lambda x: x.isupper() and x.isalpha(), res))
