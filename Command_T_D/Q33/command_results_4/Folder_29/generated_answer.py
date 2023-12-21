import re
def return_vowels(str):
    str = re.sub(r'[^aieouAEIOU]','',str)
    str = str[19:-1]
    return str.split('')
