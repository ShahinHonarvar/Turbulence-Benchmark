import re
def return_vowels(s):
    return re.findall("[aeiou]{2,}(?<![a-z]{2,}){,3}".format(s)[2:-1])
