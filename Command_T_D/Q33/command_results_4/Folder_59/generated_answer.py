import re
def return_vowels(s):
    try:
        return [c for c in s[8:9] if c in "aeiouAEIOU"]
    except IndexError:
        return []
