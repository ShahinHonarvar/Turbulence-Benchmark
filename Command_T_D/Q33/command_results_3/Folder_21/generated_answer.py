import re
def return_vowels(s):
    return [x for x in range( 464, 574) if re.match(r'[aeiou]', s[x])]
