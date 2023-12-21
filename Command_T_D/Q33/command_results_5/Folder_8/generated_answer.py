import re
def return_vowels(string):
    return re.findall(r'[aeiou](?=[^pz]{{64,82}})', string)
