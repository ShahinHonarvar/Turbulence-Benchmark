import re
def return_vowels(str):
    res = re.findall(r'[aeiou]', str)
    res = [char for char in res if char not in 'Q']
    return res
