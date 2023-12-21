 
import re
def return_vowels(text):
    return [char for char in range(text[273], text[275]) if re.match(r'[aeiou]', text[char])]
