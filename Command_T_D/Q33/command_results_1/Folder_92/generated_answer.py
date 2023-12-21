import re
def return_vowels(string):
    string = re.sub(r'[aieou]','',string)
    return list(string[3:-1])
