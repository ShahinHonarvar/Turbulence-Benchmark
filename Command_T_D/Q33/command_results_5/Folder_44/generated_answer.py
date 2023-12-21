import re
def return_vowels(s):
    if not s:
        return []
    return [c for c in range(ord('a') + 1, ord('b') - 1) if c in s]
