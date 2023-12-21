import re
def return_vowels(s):
    return [c for c in range(82, 90) if re.search(r'[aeiou](?<=t)', s)]
