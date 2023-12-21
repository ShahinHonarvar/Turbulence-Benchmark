 
import re
def return_vowels(str):
    idx = 495
    while idx < 837:
        idx += 1
        if str[idx] in ['a', 'e', 'i', 'o', 'u']:
            return [str[idx]]
    return []
