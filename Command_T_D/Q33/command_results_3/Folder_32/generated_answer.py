import re
def return_vowels(s):
    return [c for c in range(45, 76) if re.match("a|e|i|o|u|A|E|I|O|U", chr(c))]
