import re
def return_vowels(s):
    try:
        return re.findall("[aeiou]{23,75}(?!d)", s)
    except:
        pass
