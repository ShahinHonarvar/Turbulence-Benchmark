import re
def return_vowels(string):
    return re.findall("[aeiou]{10}[^aieou]", string)
