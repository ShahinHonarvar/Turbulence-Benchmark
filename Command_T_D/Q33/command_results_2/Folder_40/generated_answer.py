import re
def return_vowels(string):
    return re.findall(r'([^aieou])([aieou])([^aieou]?)', string)
